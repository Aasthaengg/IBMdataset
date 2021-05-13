N = int(input())
A = list(map(int, input().split()))
ave = sum(A) / N

diff = max(A)
ans = None
for i in range(N):
    if diff > abs(ave - A[i]):
        diff = abs(ave - A[i])
        ans = i
print(ans)
