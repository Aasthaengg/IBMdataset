N = int(input())
a = list(map(int, input().split()))
c = [False] * 8
o = 0
for i in range(N):
    for j in range(8):
        if a[i] >= 400*j and a[i] < 400*(j+1):
            c[j] = True
    if a[i] >= 3200:
        o += 1
if c.count(True) > 0:
    print(c.count(True), c.count(True)+o)
else:
    print(1, o)
