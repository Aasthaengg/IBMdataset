N=int(input())
S=input()
L=[chr(i) for i in range(97, 97+26)]
ans0 = 0

for i in range(N-1):
  s1=S[0:i+1]
  s2=S[i+1:N]
  ans = 0
  for j in L:
    if ((j in s1) & (j in s2)):
      ans = ans + 1
    #print(ans)
  if ans0 < ans:
    ans0 = ans
print(ans0)
    
