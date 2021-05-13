d,g = map(int,input().split())
P = [0]*d
C = [0]*d
for i in range(d):
    P[i],C[i] = map(int,input().split())

ans = float('inf')
for i in range(2**d):
    tmp = 0
    res = 0
    for j in range(d):
        if ((i>>j)&1):
            tmp+=C[j]+(j+1)*100*P[j]
            res+=P[j]
    if tmp<g:
        for j in range(d-1,-1,-1):
            if not ((i>>j)&1):
                if tmp>=g:
                    break
                if tmp+(j+1)*100*P[j]<=g:
                    tmp+=(j+1)*100*P[j]
                    res+=P[j]
                else:
                    for p in range(P[j]):
                        if tmp>=g:
                            break
                        tmp+=(j+1)*100
                        res+=1
    ans = min(ans,res)
print(ans)