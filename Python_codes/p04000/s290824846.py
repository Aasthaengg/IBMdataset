h,w,n=map(int,input().split())
ab=[list(map(int,input().split())) for _ in [0]*n]
ab_d={a*(10**9)+b-1 for a,b in ab}

ans=[set() for _ in range(9)]
for a,b in ab:
    temp=[None for _ in [0]*25]
    for p in range(25):
        i,j=p//5,p%5
        if 0<a+i-2<=h and 0<b+j-2<=w:
            if (a+i-2)*(10**9)+b+j-3 in ab_d:
                temp[i*5+j]=1
            else:
                temp[i*5+j]=0
    for p in range(9):
        i,j=p//3,p%3
        cnt=[temp[(i+k)*5+j+l] for k in range(3) for l in range(3)]
        if None not in cnt:
            ans[sum(cnt)-1].add((a+i-2)*(10**9)+b+j-3)
                
ans=[len(ans[i]) for i in range(9)]

print((h-2)*(w-2)-sum(ans))
for i in ans:
    print(i)