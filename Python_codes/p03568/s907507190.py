n = int(input())
a = list(map(int,input().split()))

amax = []
amin = []

for i in range(n):
    amax.append(a[i] + 1)
    amin.append(a[i] - 1)

m = 3 ** n

for z in range(3 ** n):
    asearch = []
    amulti = 1
    x = z
    for i in range(n):
        asearch.append(x % 3)
        x = x // 3
    for i in range(n):
        if asearch[i] == 0:
            amulti *= a[i]
        elif asearch[i] == 1:
            amulti *= amax[i]
        else:
            amulti *= amin[i]
    if amulti % 2 != 0:
        m -= 1

print(m)