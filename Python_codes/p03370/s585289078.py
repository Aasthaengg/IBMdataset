N, X = map(int, input().split())
m = list(int(input()) for i in range(N))
print((X - sum(m)) // min(m) + N)