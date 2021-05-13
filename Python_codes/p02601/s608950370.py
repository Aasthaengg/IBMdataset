a, b, c = map(int, input().split())
k = int(input())
for i in range(k):
    if a >= b:
        b *= 2
    elif b >= c:
        c *= 2
print('Yes') if a < b < c else print('No')