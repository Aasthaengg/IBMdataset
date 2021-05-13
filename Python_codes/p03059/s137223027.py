A, B, T = map(int, input().split())
ans = 0
cnt = A
while cnt <= T + 0.5:
    ans += B
    cnt += A
print(ans)
