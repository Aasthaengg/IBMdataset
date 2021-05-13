def comb(arr, k):
    n = len(arr)
    def dfs(curr,cnt,tmp):
        ret = []
        if cnt==0:
            return [tmp]
        for i in range(curr,n-cnt+1):
            ret += dfs(i+1,cnt-1,tmp+[arr[i]])
        return ret
    return dfs(0,k,[])

from math import *
N=int(input())
k1 = int(sqrt(2*N))
k2 = k1+1
if k1*k2 == 2*N:
    print("Yes")
    print(k2)
    ans = [[] for _ in range(k2)]
    for i, (i1, i2) in enumerate(comb(list(range(k2)), 2)):
        ans[i1].append(i+1)
        ans[i2].append(i+1)
    
    for arr in ans:
        print(" ".join([str(v) for v in [k1]+arr]))
else:
    print("No")
