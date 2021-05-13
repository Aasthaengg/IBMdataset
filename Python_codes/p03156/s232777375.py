n = int(input())
a,b = map(int, input().split())
lis = list(map(int, input().split()))

lis = sorted(lis, reverse=True)

cnt = 0
for i in range(n):
    tmp = []
    for j in lis:
        if j >= b+1:
            tmp.append(j)
            break
    for k in lis:
        if a+1 <= k <= b:
            tmp.append(k)
            break
    
    for l in lis:
        if l <= a:
            tmp.append(l)
            break
    
    if len(tmp) == 3:
        cnt += 1
    
    for x in tmp:
        lis.remove(x)

print(cnt)
