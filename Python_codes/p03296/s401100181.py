a = int(input())
b = []
c = list(map(int, input().split()))
d = 0
for i in range(1, len(c)):
    if c[i] == c[i-1]:
        d += 1
    else:
        if d != 0:
            b.append(d+1)
            d = 0
if d != 0:
    b.append(d+1)
e = 0
for i in b:
    e += i // 2
print(e)
