A, B, T = map(int, input().split())
ans = 0
time = A
while time <= T:
    ans += B
    time += A
print(ans)