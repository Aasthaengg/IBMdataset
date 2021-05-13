n , m = map(int, input().split())

lis = [list(map(int, input().split())) for _ in range(m)]
p = list(map(int, input().split()))

count = 0

for i in range(2**n):
    b = bin(i)
    sw = [False] * n
    for j in range(n):
        if (i >> j) & 1:
            sw[j] = True

    boollist = []
    for j in range(m):
        k = lis[j][0]
        sl = lis[j][1:]
        total = 0

        for x in sl:
            if sw[x-1]:
                total += 1
        
        if total % 2 == p[j]:
            boollist.append(1)
        else:
            boollist.append(0)
    
    if all(boollist):
        count += 1

print(count)