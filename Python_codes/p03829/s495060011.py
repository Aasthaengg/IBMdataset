N, A, B = [int(s) for s in input().split()]
X = [int(s) for s in input().split()]

d1 = [X[i+1] - X[i] for i in range(N-1)]
d2 = [min(d*A,B) for d in d1]

print(sum(d2))