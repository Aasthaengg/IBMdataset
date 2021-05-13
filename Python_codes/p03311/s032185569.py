N = int(input())
A = list(map(int, input().split()))

for i in range(1,N+1):
    A[i-1] -= i
A.sort()

if N % 2 == 1:
    ans = 0
    for i in A:
        ans += abs(i - A[N//2])
else:
    ans = 0
    ansk = 0
    for i in A:
        ans += abs(i - A[N//2])
        ansk += abs(i - A[N//2-1])
    ans = min(ans, ansk)

print(ans)
