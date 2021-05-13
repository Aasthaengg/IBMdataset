r, c = map(int, input().split())
matrix = []
for i in range(r):
    l = list(map(int, input().split()))
    l.append(sum(l))
    matrix.append(l)
matrix.append([sum(i) for i in zip(*matrix)])
for l in matrix:
    print(" ".join(str(n) for n in l))