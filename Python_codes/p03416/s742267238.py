L = []
for i in range(1, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            L.append(i * 10000 + j * 1000 + k * 100 + j * 10 + i)
a, b = map(int, input().split())
print(sum(i in L for i in range(a, b + 1)))
# print(sum(a <= e <= b for e in L))
