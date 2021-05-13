N, A, B = map(int, input().split())
x = list(map(int, input().split()))

ans = 0

for i in range(N-1):
    tmp = x[i+1] - x[i]
    if tmp * A > B:
        ans += B
    else:
        ans += tmp * A

print(ans)