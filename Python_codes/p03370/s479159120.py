n, x = map(int, input().split())
M = [int(input()) for _ in range(n)]
print(len(M) + (x - sum(M)) // min(M))