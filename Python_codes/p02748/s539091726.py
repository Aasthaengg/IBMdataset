a, b, M = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
ans = float('inf')
for _ in range(M):
    x, y, c = [int(i) for i in input().split()]
    ans = min(ans, A[x-1] + B[y-1] - c)
ans = min(ans, min(A)+min(B))
print(ans)
