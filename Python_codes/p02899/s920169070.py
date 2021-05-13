N = int(input())
A = list(map(int, input().split()))
D = {i: j for i, j in enumerate(A, 1)}
D = sorted(D.items(), key = lambda x: x[1])
print(*list(x[0] for x in D))