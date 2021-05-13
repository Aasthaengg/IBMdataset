A = list(map(int,input().split()))
A.sort()
k = int(input())
ans = sum(A[:2]) + A[2]*(2**k)
print(ans)

