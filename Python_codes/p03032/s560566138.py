[n,k],li = [list(map(int,i.split())) for i in open(0)] 
ans = 0
for i in range(1,min(n+1,k+1)):
    for j in range(i+1):
        l = li[:(i-j)] + li[n-j:]
        re_num = min(k-i,len(l))
        l.sort()
        f = 0
        for p in range(re_num):
            if l[p] > 0:
                break
            f += 1
        l = l[f:]
        ans = max(ans,sum(l))
print(ans)