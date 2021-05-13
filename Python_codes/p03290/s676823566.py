d,g = map(int,input().split())
p = []
c = []
for i in range(d):
    x,y = map(int,input().split())
    p.append(x)
    c.append(y)

ans = 10**3+1
for i in range(2**d):
    tmp = 0
    tmp_ans = 0
    t = [0]*d
    for j in range(d):
        if (i>>j)&1:
            tmp += 100*(j+1)*p[j] + c[j]
            tmp_ans += p[j]
            t[j] = 1
    if tmp < g:
        for k in range(d-1,-1,-1):
            if t[k] == 0:
                if tmp+100*(k+1)*(p[k]-1) < g:
                    tmp_ans += 10**3+1
                else:
                    if (g-tmp)%(100*(k+1)) == 0:
                        tmp_ans += (g-tmp)//(100*(k+1))
                    else:
                        tmp_ans += (g-tmp)//(100*(k+1))+1
                break
    ans = min(tmp_ans,ans)

print(ans)
