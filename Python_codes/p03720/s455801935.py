n, m = map(int, input().split(" "))
nn = [0 for i in range(n)]
for i in range(m):
    a, b = map(int, input().split(" "))
    nn[a - 1] += 1
    nn[b - 1] += 1
for i in nn:
    print(i)
