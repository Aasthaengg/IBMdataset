N, A, B = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(N-1):
    if (arr[i+1] - arr[i]) * A > B:
        ans += B
    else:
        ans += (arr[i+1] - arr[i]) * A
print(ans)