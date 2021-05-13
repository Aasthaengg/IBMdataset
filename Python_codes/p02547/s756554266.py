n = int(input())
c, d = [], []
for i in range(n):
    a, b = [int(i) for i in input().split()]
    c.append(a)
    d.append(b)

count = 0

for i in range(0, n):
    if c[i] == d[i]:
        count += 1
    else:
        count = 0
    if count == 3:
        break

if count == 3:
    print('Yes')

else:
    print('No')
