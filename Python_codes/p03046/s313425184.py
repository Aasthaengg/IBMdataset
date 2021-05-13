import sys
m, k = map(int, input().split())

if (m == 1 and k == 1) or (2 ** m <= k):
    print(-1)
    sys.exit()

if m == 1 and k == 0:
    print('1 1 0 0')
    sys.exit()

if m == 0 and k == 0:
    print('0 0')
    sys.exit()

f = 1
p = 0
p2 = []

for i in range(2 ** m):
    if i == k:
        continue
    else:
        if f:
            p = i
            f = 0
        else:
            p2.append(i)

ans = [p, k, p] + p2 + [k] + list(reversed(p2))
print(' '.join(list(map(str, ans))))

