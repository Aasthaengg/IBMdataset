N, H = map(int, input().split())
ab = [[int(i) for i in input().split()] for _ in range(N)]

a = 0
for i in range(N):
    a = max(a, ab[i][0])

b = []
for i in range(N):
    if ab[i][1] > a:
        b.append(ab[i][1])
b.sort(reverse=True)

w = True
c = 0
h = H
for i in range(len(b)):
    h -= b[i]
    c += 1
    if h <= 0:
        print(c)
        w = False
        break

if w:
    print(c + (h-1)//a + 1)
