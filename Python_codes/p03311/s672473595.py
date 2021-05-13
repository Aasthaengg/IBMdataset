N = int(input())
A = list(map(int, input().split()))
for i in range(1, N+1):
    A[i-1] = A[i-1]-i
A.sort()
number = A[N//2]
ans = 0
for i in range(0, N):
    ans += abs(A[i]-number)
print(ans)
