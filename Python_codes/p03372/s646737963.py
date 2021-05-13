n,c = map(int, input().split())
xv=[list(map(int,input().split())) for i in range(n)]

def solve(xv):
    lis = [0] * n # best score in x sushi
    now_v=0
    best=0

    for i in range(n):
        x,v = xv[i]
        now_v+=v
        best=max(best,now_v - x)
        lis[i] = best

    lis.insert(0,0)
    ans=max(lis)

    now_v=0
    for i in reversed(range(n)):
        x,v = xv[i]
        now_v+=v
        ans=max(ans,now_v-2*(c-x) + lis[i])

    return ans


xv2 = []
for i in reversed(range(n)):
    x,v = xv[i]
    x=c-x
    xv2.append([x,v])

ans = max(solve(xv),solve(xv2))

print(ans)