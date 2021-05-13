n,m = map(int,input().split())
li = []
for i in range(n):
    li.append(list(map(int,input().split())))
lia = sorted(li, key=lambda x:(x[0],x[1]))
asum = 0
for i in range(n):
    if m >= lia[i][1]:
        m -= lia[i][1]
        asum += lia[i][0]*lia[i][1]
    else:
        asum += lia[i][0]*m
        break
print(asum)