X, Y = map(int, input().split())
ans = 10**10
if Y-X >= 0:
    ans = min(ans, Y-X)
if Y+X >= 0:
    ans = min(ans, Y+X+1)
if -Y-X >= 0:
    ans = min(ans, -Y-X+1)
if -Y+X >= 0:
    ans = min(ans, -Y+X+2)
print(ans)
