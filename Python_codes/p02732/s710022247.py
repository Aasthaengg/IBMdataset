from collections import defaultdict

n = int(input())
a = [int(x) for x in input().split()]

cnt = defaultdict(int)
for v in a:
  cnt[v] += 1

ans = 0
for v in cnt:
  ans += cnt[v]*(cnt[v]-1)//2

for v in a:
  print(ans + (cnt[v]-1)*(cnt[v]-2)//2 - cnt[v]*(cnt[v]-1)//2)