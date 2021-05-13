n = int(input())
a = 0
for x in range(1, 9 + 1):
    for y in range(1, 9 + 1):
        if x * y == n:
            a = True

if a:
    print('Yes')
else:
    print('No')