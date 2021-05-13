a, b, c = map(int,input().split())
count = 0
#偶奇を一致させる
if a % 2 == b % 2 == c % 2:
    count = 0

elif a % 2 == b % 2 != c % 2:
    count += 1
    a += 1
    b += 1

elif b % 2 == c % 2 != a % 2:
    count += 1
    b += 1
    c += 1

elif a % 2 == c % 2 != b % 2:
    count += 1
    a += 1
    c += 1
maxnum = max(a, b, c)

while a < maxnum:
    a += 2
    count += 1

while b < maxnum:
    b += 2
    count += 1

while c < maxnum:
    c += 2
    count += 1

print(count)