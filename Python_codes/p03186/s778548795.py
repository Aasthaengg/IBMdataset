
a, b, c = map(int, input().split())

if a+b+1 > c:
    count = b+c
else:
    count = b+(a+b+1)

print(count)