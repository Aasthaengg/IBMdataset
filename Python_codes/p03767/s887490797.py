N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
ans = 0

ans = sum(A[1:2*N:2])
print(ans)
