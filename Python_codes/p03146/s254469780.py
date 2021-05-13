ans = 1

s = int(input())
l = {s}

while True:
    ans += 1
    if s % 2 == 0:
        s //= 2
    else:
        s = 3 * s + 1
    if s in l:
        print(ans)
        break
    l.add(s)