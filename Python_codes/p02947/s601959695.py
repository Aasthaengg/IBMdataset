from collections import defaultdict

n=int(input())
h=defaultdict(int)
for i in range(n):
  s=list(input().strip())
  s.sort()
  h["".join(s)]+=1

ans=0
for v in h.values():
  if v>1:
    ans += v*(v-1)//2
print(ans)