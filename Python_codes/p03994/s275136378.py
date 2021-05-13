al=[chr(ord('a') + i) for i in range(26)]
s=input()
N=len(s)
K=int(input())

for i in range(N):
  if i<N-1:
    a=26-al.index(s[i])
    if K>=a and s[i]!="a":
      K -= a
      s=s[0:i]+al[(al.index(s[i])+a)%26]+s[i+1:]
  else:
    K %= 26
    p= (K+al.index(s[i]))% 26
    s=s[0:N-1]+al[p]
    K=0
    
print(s)