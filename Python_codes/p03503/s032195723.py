n = int(input())
f = []
for i in range(n):
    f.append(list(map(int,input().split())))
p = []
for i in range(n):
    p.append(list(map(int,input().split())))

ans = -(int(1e9) + 7)
#print(ans)
for i in range(2 ** 10):
    d = [False] * 10
    for j in range(10):
        if i >> j & 1:
            d[j] = True
    if not True in d:
        continue

    val = 0
    for j in range(n):
        cnt = 0
        for k in range(10):
            if d[k] == True and f[j][k] == 1:
                cnt += 1
        val += p[j][cnt]
        #print(ans)
    ans = max(ans,val)
print(ans)
