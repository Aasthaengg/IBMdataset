import sys 
sys.setrecursionlimit(2*100000) 

def dfs(i,pre,n,a,ans):
    if (pre*2 < a[i]): return -1
    ans[i] += a[i]
    if (i >= n):
        return a[i]

    pre = pre*2 - a[i]
    u = dfs(i+1,pre,n,a,ans);
    if (u<0 or pre*2 < u): return -1;
    ans[i] += min(pre, u)
    return min(pre, u) + a[i]



n = int(input())
a = list(map(int,input().split()))

if (n == 0):
    if (a[0] == 1):
        print(1)
    else:
        print(-1)
    exit()

ans = [1] + [0]*n
u = dfs(1,1,n,a,ans)
if (a[0] != 0): u = -1

if (u >= 0):
    print(sum(ans))
else:
    print(-1)
