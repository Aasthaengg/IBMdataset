x, y, z, k = map(int, input().split())
a = map(int, input().split())
b = list(map(int, input().split()))
c = map(int, input().split())
d = sorted((ai + bi for ai in a for bi in b), reverse=True)[:k]
e = sorted((ci + di for ci in c for di in d), reverse=True)[:k]
print(*e)
