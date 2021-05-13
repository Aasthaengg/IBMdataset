a, b, c = map(int, input().split())
k = int(input())

while a >= b and k >= 0:
    k -= 1
    b *= 2

while b >= c and k >= 0:
    k -= 1
    c *= 2

if k >= 0:
    print('Yes')
else:
    print('No')