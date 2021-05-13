n = int(input())
A = list(map(int, input().split()))
#ans = [sum(A)-2*sum(A[::2])] + [0]*(n-1)
ans = [2*sum(A[::2])-sum(A)] + [0]*(n-1)
for i in range(1,n):
    ans[i] = 2*A[i-1]-ans[i-1]
print(*ans)