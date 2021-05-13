n=int(input())
s=[0]*n
t=0
for i in range(n):
  a,b=map(int,input().split())
  s[i]=a+b
  t+=b
s.sort()
s=s[::-1]
print(sum(s[::2])-t)