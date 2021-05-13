n = int(input())
spi = []
for i in range(n):
    s,p = input().split()
    spi.append([s,int(p), i+1])
spi.sort()
before = spi[0][0]
ans = [spi[0][2]]
for s,p,i in spi[1:]:
    if s == before:
        ans.append(i)
    else:
        for x in ans[::-1]:
            print(x)
        before = s
        ans = [i]
for x in ans[::-1]:
    print(x)