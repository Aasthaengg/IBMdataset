import sys
input = sys.stdin.readline

N, C, K = map(int, input().split())
T = sorted([int(input()) for _ in range(N)])

tmp, cnt, ans = 0, 0, 0
for t in T:
  if not tmp:
    tmp = t + K
    cnt += 1
    ans += 1
  elif tmp < t or cnt == C:
    tmp = t + K
    cnt = 1
    ans += 1
  else:
    cnt += 1
    
print(ans)
