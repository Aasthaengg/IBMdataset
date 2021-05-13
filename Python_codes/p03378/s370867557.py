N, M, X = map(int, input().split())
A = list(map(int, input().split()))

lst = [0]*(N+1)

for i in range(M):
    lst[A[i]] = 1

left = sum(lst[0:X])
right = sum(lst[X:N+1])
ans = min(left, right)
print(ans)
