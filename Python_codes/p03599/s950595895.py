import sys
readline = sys.stdin.readline

# A + Bの組み合わせはせいぜい1～30のうち作れる数字のみなので全探索

A,B,C,D,E,F = map(int,readline().split())

ans = [0,0]
maxrate = 0.0
for a in range(0,F,100 * A):
  for b in range(0,F,100 * B):
    if a == 0 and b == 0:
      continue
    if a + b > F:
      break
    water = a + b
    # waterに対して溶ける最大量は (a + b) * E
    limit = min(((a + b) // 100) * E, F - water)
    maxsugar = 0
    for c in range(0,limit + 1,C):
      for d in range(0,limit + 1,D):
        if c + d > limit:
          break
        if c + d > maxsugar:
          maxsugar = c + d
          rate = maxsugar / (water + maxsugar)
          if rate > maxrate:
            maxrate = rate
            ans = [water + maxsugar, maxsugar]

if maxrate == 0.0:
  print(min(A,B) * 100, 0)
  exit(0)

print(*ans)