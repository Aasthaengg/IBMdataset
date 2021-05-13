K, T = map(int, input().split())
A = list(map(int, input().split()))

print(max(max(A) - (K - max(A) + 1), 0))