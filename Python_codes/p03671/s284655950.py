a, b, c = map(int, input().split())
min = a+b
if min > b+c:
    min = b+c

if min > a+c:
    min = a+c

print(min)