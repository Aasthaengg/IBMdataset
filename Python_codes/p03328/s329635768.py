a, b = map(int, input().split())
h = 0
hs = []
for i in range(1, 1000):
    h += i
    hs.append(h)
for i in range(998):
    if (hs[i] - a) == (hs[i + 1] - b):
        print(hs[i] - a)
        exit()
