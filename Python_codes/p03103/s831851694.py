n,m = map(int,input().split())

array = []
[array.append(list(map(int,input().split()))) for x in range(n)]

total = 0

array.sort()

for yen,num in array:
    if num < m:
        total += yen*num
        m -= num
    else:
        total += yen*m
        break
print(total)
