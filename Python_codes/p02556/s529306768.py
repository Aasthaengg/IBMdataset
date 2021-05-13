n = int(input())
l, l2 = [], []
for i in range(n):
    x, y = map(int, input().split())
    l.append(x + y)
    l2.append(x - y)
print(max(max(l) - min(l), max(l2) - min(l2)))