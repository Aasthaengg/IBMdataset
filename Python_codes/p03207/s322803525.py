def actual(n, P):
    return int(sum(P) - (max(P) // 2))

n = int(input())
P = [int(input()) for _ in range(n)]

print(actual(n, P))