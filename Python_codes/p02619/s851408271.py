D = int(input())
c = list(map(int, input().split()))
s = []
for i in range(D):
    s.append(list(map(int, input().split())))
t = []
for i in range(D):
    t.append(int(input()))

a = [0]*26
total = 0
for i in range(D):
    ts = t[i]

    a[ts-1] = i+1
    cs = sum([x * (i+1 - y) for x, y in zip(c, a)])

    total = total + s[i][ts-1] - cs
    print(total)