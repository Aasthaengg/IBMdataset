N = int(input())
P = [int(input()) for _ in range(N)]
max_p = max(P)
sum_p = sum(P)
print(sum_p - (max_p//2))