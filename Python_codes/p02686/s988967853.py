n = int(input())

x = []
y = []
# left >= rightの場合、
# keft < right う

for _ in range(n):
    s = input()
    b = c = 0

    # sの中でペアにならない括弧を計算
    for t in s:
        if t == '(':
            b += 1
        else:
            if b == 0:
                c += 1
            else:
                b -= 1
    if b >= c:
        x.append((c, b))
    else:
        y.append((-b, c))
x.sort()
y.sort()
now = 0
for a, b in x:
    now -= a
    if now < 0:
        print('No')
        exit()
    now += b
for a, b in y:
    now -= b
    if now < 0:
        print('No')
        exit()
    now -= a

if now == 0:
    print('Yes')
else:
    print('No')
