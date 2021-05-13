N = int(input())
B = list(map(int, input().split()))
if N > 2:
    ans = B[0]
    for i in range(1, N-1):
        if i == N-2:
            ans += B[i]
        ans += min(B[i-1], B[i])
else:
    ans = 2*B[0]
print(ans)