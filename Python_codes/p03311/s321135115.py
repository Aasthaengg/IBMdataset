N = int(input())
A = [int(i) for i in input().split()]

B = [a - i for i, a in enumerate(A)]
B.sort()
median = B[(N - 1) // 2]
print(sum(abs(b - median) for b in B))
