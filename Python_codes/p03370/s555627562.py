N, X = map(int, input().split())
m = [int(input()) for i in range(N)]
sum_m = sum(m)
min_m = min(m)
current = N
print(current + (X - sum_m) // min_m)
