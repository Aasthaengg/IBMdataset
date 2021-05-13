import sys
input = sys.stdin.readline
X,Y = map(int,input().rstrip().split())
ans = 0
while True:
  if X <= Y:
    ans += 1
    X = 2*X
  else:
    break
print(ans)