# ABC125B

n = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))
x = 0
y = 0
for v, c in zip(V, C):
    if v > c:
        x += v
        y += c
print(abs(x - y))
