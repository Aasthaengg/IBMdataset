n = int(input())
a, b, c = map(str, [input() for i in range(3)])
#print(n, a, b, c)
result = ""
sum = 0

def count_same(ca, cb, cc):
    ct = 0
    if ca == cb == cc:
        return 3
    if ca == cb:
        return ca
    if cb == cc:
        return cb
    if cc == ca:
        return cc
    return 0
for i in range(n):
    tmp = count_same(a[i], b[i], c[i])
    if tmp == 3:
        result += a[i]
    elif tmp == 0:
        result += a[i]
        sum += 2
    else:
        result += tmp
        sum += 1

print(sum)