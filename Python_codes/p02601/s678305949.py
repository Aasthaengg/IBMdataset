a, b, c = map(int, input().split())

k = int(input())

times = 0

while a >= b:
    b *= 2
    times += 1

while b >= c:
    c *= 2
    times += 1

if times <= k:
    print('Yes')

else:
    print('No')
