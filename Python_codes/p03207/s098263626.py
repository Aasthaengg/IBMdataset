n = int(input())
p = [int(input()) for _ in range(n)]
mp = max(p)
print((sum(p)-mp) + (mp//2))