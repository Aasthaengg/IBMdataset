N = int(input())
p = [int(input()) for _ in range(N)]
print(max(p)//2 + sum(p) - max(p))