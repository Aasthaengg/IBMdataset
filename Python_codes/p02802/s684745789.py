n,m = list(map(int,input().split()))
ans = [0,0]
p_list = [0]*(n+1)
ac = [0]*(n+1)
for i in range(m):
    ps = input().split()
    p = int(ps[0])
    s = ps[1]
    if s=='AC' and ac[p]==0:
        ans[0] += 1
        ans[1] += p_list[p]
        ac[p] += 1
    else:
        if ac[p]==0:
            p_list[p] += 1
print(*ans, sep=' ')