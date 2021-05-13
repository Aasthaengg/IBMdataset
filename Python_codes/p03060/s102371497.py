N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

total = 0
for x, y in zip(V, C):
    if x - y > 0:
        total += x - y
print(total)
