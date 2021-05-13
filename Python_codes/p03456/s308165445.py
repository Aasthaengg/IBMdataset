a, b = [str(n) for n in input().split()]

c = int(a + b)

for n in range(c//2):
    p = n * n
    if p == c:
        print('Yes')
        exit()
    if p > c:
        break
print('No')
