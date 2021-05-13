N, M = [int(i) for i in input().split(' ')]
A = [int(i) for i in input().split(' ')]
r = N - sum(A)
print(r if r >= 0 else -1)
