x, y, z = map(int, input().split())
c = 0
for i in range(x, y+1):
    if z % i == 0:
        c += 1
print (c)
