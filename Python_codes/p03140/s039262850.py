from collections import Counter

N=int(input())
A=input()
B=input()
C=input()

D=[]
for i in range(N):
  mc = Counter([A[i],B[i],C[i]]).most_common()[0][0]
  D.append(mc)
D=''.join(D)
  
def diff(s1,s2):
  out=0
  for i in range(len(s1)):
    if s1[i] != s2[i]:
      out += 1
  return out

ans=0
ans+=diff(D,A)
ans+=diff(D,B)
ans+=diff(D,C)

print(ans)