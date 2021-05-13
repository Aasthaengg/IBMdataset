N = int(input())
A = list(map(int, input().split()))
X = sorted([[i+1, A[i]] for i in range(N)], key=lambda x: x[1])
print(*[x[0] for x in X])