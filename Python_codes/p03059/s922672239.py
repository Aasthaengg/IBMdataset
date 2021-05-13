a, b, t = map(int, input().split())
time = 0
ans = 0
while time+a < t+0.5:
    ans += b
    time += a
print(ans)
