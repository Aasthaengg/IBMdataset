n = int(input())
alst = list(map(int, input().split()))
alst.sort()
pos = 0
total = 0
for i, a in enumerate(alst):
    if a > total * 2:
        pos = i
    total += a
print(n - pos)