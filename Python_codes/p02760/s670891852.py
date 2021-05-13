a = []
for _ in range(3):
    a += list(map(int, input().split()))

n = int(input())
for _ in range(n):
    b = int(input())
    for i in range(9):
        if a[i] == b:
            a[i] = 0

# print(a)
for i in range(3):
    if sum(a[i*3:i*3+3]) == 0:
        print('Yes')
        exit()
    if sum(a[i:9:3]) == 0:
        print('Yes')
        exit()

if (a[0] + a[4] + a[8]) == 0:
    print('Yes')
    exit()
if (a[2] + a[4] + a[6]) == 0:
    print('Yes')
    exit()

print('No')