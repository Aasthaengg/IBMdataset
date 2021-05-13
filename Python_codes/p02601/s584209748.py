a, b, c = map(int, input().split())
k = int(input())

i = 0
while not a < b:
    b *= 2
    i += 1
while not b < c:
    c *= 2
    i += 1

if i <= k:
    print('Yes')
else:
    print('No')