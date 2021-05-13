
ri = lambda S: [int(v) for v in S.split()]

N, M = ri(input())
A = ri(input())
s = sum(A)
print(N - s if N - s >= 0 else -1)