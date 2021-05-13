n, m = map(int, input().split())

pena = [0]*(10**5 + 1)

wa = 0
ac = 0

for i in range(m):
    p, s = map(str, input().split())
    if s == "WA" and pena[int(p)] != -1:
        pena[int(p)] += 1
    elif s == "WA" and pena[int(p)] == -1:
        continue
    elif s == "AC" and pena[int(p)] == -1:
        continue
    else:
        ac += 1
        wa += pena[int(p)]
        pena[int(p)] = -1

print("{} {}".format(ac, wa))
