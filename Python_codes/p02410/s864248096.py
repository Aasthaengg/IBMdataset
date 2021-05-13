m1 = []
m2 = []
n, m = [int(s) for s in input().split()]
for i in range(n):
    m1.append([int(s) for s in input().split()])

for i in range(m):
    m2.append(int(input()))

for ma in m1:
    print(sum(map(lambda m, n: m * n, ma, m2)))