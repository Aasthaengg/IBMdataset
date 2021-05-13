N, M = map(int, input().split())
A = sum(list(map(int, input().split())))
print(N-A if N>=A else -1)