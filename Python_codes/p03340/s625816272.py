n=int(input())
a_list=list(map(int,input().split()))
A_list=[format(a_list[i],'b').zfill(20) for i in range(n)]
count=[0]*20
r=0
ans=0
for l in range(n):
    while not 2 in count and r<=n-1:
        for j in range(20):
            count[j]=count[j]+int(A_list[r][j])
        r=r+1
    if not 2 in count:
        ans=ans+n-l
    else:
        ans=ans+r-l-1
    for j in range(20):
        count[j]=count[j]-int(A_list[l][j])
print(ans)

    
