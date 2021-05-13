d,g = map(int,input().split())
pc = []
for i in range(d):
    p,c = map(int,input().split())
    pc.append([p,c])
ans = 10 ** 18
for bit in range(2**d):
    count = 0
    sump = 0
    se = set()
    for i in range(d):
        if bit >> i & 1:
            sump += pc[i][0]*(i+1)*100 + pc[i][1]
            count += pc[i][0]
        else:
            se.add(i+1)
    if sump >=g:
        ans=min(ans,count)
    else:
        s = max(se)
        tmp = min(pc[s-1][0],((g-sump+100*s-1)//(100*s)))
        count += tmp
        sump+=tmp*s*100
        if sump>=g:
            ans=min(ans,count)
print(ans)