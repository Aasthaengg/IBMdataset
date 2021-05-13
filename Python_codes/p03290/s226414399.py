d,g = map(int,input().split())
P = [0]*d
C = [0]*d
for i in range(d):
    P[i],C[i] = map(int,input().split())

ans = float('inf')
bit_n = d
for i in range(2**d):
    tmp = 0
    solved = 0
    for j in range(d):
        if ((i>>j)&1):
            tmp+=C[j]
            tmp+=(j+1)*100*P[j]
            solved+=P[j]
    if tmp>=g:
        ans = min(ans,solved)
    else:
        for j in range(d-1,-1,-1):
            if tmp>=g:
                ans = min(ans,solved)
                break
            if not ((i>>j)&1):
                for k in range(P[j]):                 
                    if tmp>=g:
                        ans = min(ans,solved)
                        break
                    solved+=1
                    tmp+=(j+1)*100
print(ans)