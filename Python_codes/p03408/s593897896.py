from collections import defaultdict
dd=defaultdict(int)

N=int(input())
for _ in range(N):
  dd[input()]+=1

M=int(input())
for _ in range(M):
  dd[input()]-=1

ans=max(dd.values())
ans=max(ans, 0)
print(ans)