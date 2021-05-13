n,a,b,c = map(int,input().split())
l = []
for i in range(n):
    l.append(int(input()))
mi = 10**18
aa = []
ba = []
ca = []
da = []
def dfs(ai,bi,ci,di,i):
    global mi
    if i == n:
        if len(ai) == 0 or len(bi) == 0 or len(ci) == 0:
            return mi
        tmp = 0
        if len(ai) > 1:
            tmp += 10 * (len(ai) - 1)
        if len(bi) > 1:
            tmp += 10 * (len(bi) - 1)
        if len(ci) > 1:
            tmp += 10 * (len(ci) - 1)
        tmp += abs(a - sum(ai))
        tmp += abs(b - sum(bi))
        tmp += abs(c - sum(ci))
        mi = min(mi,tmp)
        return mi
    else:
        return min(min(dfs(ai+[l[i]],bi,ci,di,i+1),dfs(ai,bi+[l[i]],ci,di,i+1)),min(dfs(ai,bi,ci+[l[i]],di,i+1),dfs(ai,bi,ci,di+[l[i]],i+1)))
print(dfs(aa,ba,ca,da,0))