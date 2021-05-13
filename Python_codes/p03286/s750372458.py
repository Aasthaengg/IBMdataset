n = int(input())
if n == 0:
    print(0)
    exit()
d = []
while n != 0:
    p = n % 2
    d.append(p)
    n = (n - p) * (-1) // 2
for u in reversed(d):
    print(u, end='')
print()
