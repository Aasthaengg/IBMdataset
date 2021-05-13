n = int(input())

def hs(k):
    ks = str(k)
    lk = len(ks)
    a = int(ks[0])
    b = int(ks[len(ks) - 1])
    if lk == 1:
        return 1
    if b == 0:
        return 0
    s = 0
    if (a > b) & (lk > 1):
        s += 10 ** (lk - 2) * 2
    elif a == b:
        if lk == 2:
            s += 1
        else:
            s += ((k % (a * 10**(lk - 1))) // 10 + 1) * 2 - 1
    if lk >= 2:
        for i in range(lk - 1):
            if lk - i - 3 >= 0:
                s += 10 ** (lk - 3 - i) * 2
            elif a == b:
                s += 2
    return s

ans = 0
for i in range(1, n + 1):
    ans += hs(i)
print(ans)