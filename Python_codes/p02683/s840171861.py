n,m,x = map(int,input().split())
ca = [list(map(int,input().split())) for i in range(n)]
ans = 100000000
for bit in range(1 << n):
    tmp_ca = [0] * (m+1)
    for j in range(n):
        if bit & (1 << j):
            for k in range(m+1):
                tmp_ca[k] += ca[j][k]
        tmp = 0
        for k in range(1,m+1):
            if tmp_ca[k] < x:
                tmp += 1
        if tmp == 0:
            ans = min(ans,tmp_ca[0])
if ans == 100000000:
    print(-1)
else:
    print(ans)
