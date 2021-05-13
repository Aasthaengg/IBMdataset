n = int(input())
spi = []
for i in range(n):
    s,p = input().split()
    p = 100-int(p)
    spi.append([s,p,i+1])
spi.sort()
for x in spi:print(x[-1])