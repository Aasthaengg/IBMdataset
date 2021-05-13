N = int(input())
*A, = map(int, input().split())
B = sorted([j-i for i, j in enumerate(A, start=1)])
b = B[N//2]
print(sum(abs(i-b) for i in B))
