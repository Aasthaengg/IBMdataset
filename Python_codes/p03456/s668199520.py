a, b = input().split()
t = int(a + b)
for i in range(1,10 ** 3):
    if t == (i * i):
        print('Yes')
        exit(0)
print('No')
