N, A, B = map(int, input().split())
num = list(map(int, input().split()))

ans = 0
for i in range(1, N):
    d = num[i] - num[i-1]
    if d*A < B:
       ans += d*A
    else:
        ans += B

print(ans)
