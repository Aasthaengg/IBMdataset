N, x = map(int, input().split())
lis = list(map(int, input().split()))
c = 0

lis.sort()
for i in lis:
    x -= i
    if x >= 0:
        c += 1
    else:
        break

if x > 0:
    c -= 1

print(c)
