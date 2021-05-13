n, t = map(int, input().split())

ans = 1001
for i in range(n):
    a, b = map(int, input().split())
    if b <= t and a < ans:
        ans = a

print(ans if ans != 1001 else "TLE")