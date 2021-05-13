n = int(input())
p = sorted([int(input()) for _ in range(n)])
print(sum(p, -p[-1]//2))