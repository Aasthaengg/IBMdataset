n, m, l = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
b = [list(map(int, input().split())) for i in range(m)]

for i in a:
    result = []
    for j in zip(*b):
        result.append(sum([a * b for (a,b) in zip(i, j)]))
    print(*result)