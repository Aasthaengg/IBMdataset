from collections import defaultdict

N=int(input())
*A,=map(int,input().split())

like=defaultdict(set)
ans=0
for i in range(N):
  if A[i] in like[i+1]:
    ans += 1
  like[A[i]].add(i+1)
  
print(ans)