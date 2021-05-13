a, b = input().split()
n = int(a + b)
for i in range(1, n):
    if i**2 == n:
        print('Yes')
        exit()
print('No')