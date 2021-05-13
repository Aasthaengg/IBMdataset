A = [int(x) for x in input().split()]
k = int(input())

A.sort()

ans = sum(A[0:2]) + A[2] * 2 ** (k)
print(ans)