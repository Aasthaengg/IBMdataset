n,W = map(int,input().split())
a = {}
for i in range(n):
    w,v = map(int,input().split())
    a.setdefault(w, []).append(v)

we = [0]*4
va = []
num = [0]*4
for i,[k,v] in enumerate(a.items()):
    we[i] = k
    va.append(sorted(v,reverse=True))
    num[i] = len(v)
for i in range(4-len(va)):
    va.append([0])

ans = -float('inf')
for i in range(max(1,num[0]+1)):
    for j in range(max(1,num[1]+1)):
        for k in range(max(1,num[2]+1)):
            for l in range(max(1,num[3]+1)):
                if we[0]*i + we[1]*j + we[2]*k + we[3]*l <= W:
                    total = 0
                    for im,m in enumerate([i,j,k,l]):
                        total += sum(va[im][:m])
                    ans = max(ans, total)
print(ans)