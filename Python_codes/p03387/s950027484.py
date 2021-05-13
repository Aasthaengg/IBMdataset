k = sorted(map(int, input().split()))
a = k[0]
b = k[1]
c = k[2]

cnt = 0
if a%2 != b%2:
    c += 1
    a += 1
    cnt += 1

while True:
    if a == c or b == c:
        break
    a += 1
    b += 1
    cnt += 1
if a == c:
    print(cnt)
else:
    print(cnt+(c-a)//2)