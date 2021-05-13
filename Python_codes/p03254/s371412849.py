import sys
N, x = map(int,input().split())
aN = list(map(int,input().split()))

aN.sort()
ans = 0
for n in range(N):
  if x >= aN[n]:
    ans += 1
    x -= aN[n]
  else:
    print(ans)
    sys.exit()
print(N if x == 0 else N-1)
