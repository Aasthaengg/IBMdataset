h, w = map(int, input().split())
c = list(input() for i in range(h))
for i in range(h):
    for j in range(w):
        print(c[i][j], end='')
    print()
    for j in range(w):
        print(c[i][j], end='')
    print()
