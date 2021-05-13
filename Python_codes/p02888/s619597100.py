from bisect import bisect_left
N = int(input())
A = sorted(map(int, input().split()))

ans = 0
for i in range(N):
    for j in range(i+1, N):
        r = bisect_left(A, A[i]+A[j])
        ans += r-(j+1)

print(ans)
