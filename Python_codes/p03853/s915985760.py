h, w = map(int, input().split())
c = []
for i in range(h):
    c.append(input())
thined_c = [0] * (2 * h)
for i in range(2 * h):
    s = ''
    for j in range(w):
        s += c[i // 2][j]
    thined_c[i] = s
for s in thined_c:
    print(s)
