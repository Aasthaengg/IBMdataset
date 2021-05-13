import collections
N = int(input())
a = list(map(int,input().split()))
ans = sum(a)
cnt = collections.Counter(a)
for i in range(int(input())):
  b,c = map(int,input().split())
  ans += (c-b)*cnt[b]
  cnt[c] += cnt[b]
  cnt[b] = 0
  print(ans)