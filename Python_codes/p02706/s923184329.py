N, M = map(int, input().split())
A = map(int, input().split())
print(max(N - sum(A), -1))