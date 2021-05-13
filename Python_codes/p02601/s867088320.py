a, b, c = map(int, input().split())
k = int(input())
while k>0 and not (a<b<c):
    if a>=b:
        b *= 2
        k -= 1
    elif b>=c:
        c *= 2
        k -= 1
print('Yes' if a<b<c else 'No')