a, b, c = map(int, input().split())
k = int(input())

r = 0
while a >= b:
    r += 1
    b *= 2
    if r > k:
        break
while b >= c:
    r += 1
    c *= 2
    if r > k:
        break
if r <= k:
    print('Yes')
else:
    print('No')