from collections import Counter
N=int(input())
A=list(map(int, input().split()))
C=Counter(A)
L=[]
R=[]
for i in C:
  l=C.get(i)
  if l>=2:
    L.append(i)
    if l>=4:
      R.append(i)
L.sort()
R.sort()

ans=0

if len(L)>=2:
  ans=max(L[-1]*L[-2], ans)
if len(R)>=1:
  ans=max(R[-1]**2, ans)
print(ans)
