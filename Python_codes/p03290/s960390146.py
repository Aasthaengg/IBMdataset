d, g = map(int, input().split())
PC = []
for i in range(d):
    p, c = map(int, input().split())
    PC.append((p, c))

PC.reverse()

ans = 10**18
for i in range(2**d):
    temp = 0
    cnt = 0
    flag = True
    for j in range(d):
        if (i >> j) & 1:
            temp += 100*(d-j)*PC[j][0]+PC[j][1]
            cnt += PC[j][0]
    for j in range(d):
        if not ((i >> j) & 1):
            t = 100*(d-j)
            r = g-temp
            if r > 0:
                q = (r+t-1)//t
                if q < PC[j][0]:
                    temp += 100*(d-j)*q
                    cnt += q
                else:
                    flag = False
    if flag and temp >= g:
        ans = min(ans, cnt)
print(ans)
