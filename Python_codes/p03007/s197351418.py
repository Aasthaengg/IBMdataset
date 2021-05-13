n = int(input())
a = list(map(int, input().split()))
a.sort()

print(a[-1] - a[0] + sum(map(abs, a[1:-1])))

pos = [a[-1]]
neg = [a[0]]
for x in a[1:-1]:
    if x > 0:
        pos.append(x)
    else:
        neg.append(x)
now = neg[0]
for p in pos[1:]:
    print(now, p)
    now -= p
print(pos[0], now)
now = pos[0] - now
for n in neg[1:]:
    print(now, n)
    now -= n
