x, y = map(int, input().split())

if (y % 2) != 0:
    print('No')
    exit()

for i in range(x+1):
    j = x - i
    if i * 2 + j * 4 == y:
        print('Yes')
        exit()
print('No')