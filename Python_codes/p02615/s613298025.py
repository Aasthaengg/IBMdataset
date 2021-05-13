N=int(input())
A=list(map(int,input().split()))
A=sorted(A)[::-1]
num=0
ans=0
cnt=1
i=0
while cnt<N:
    if i==0:
        ans+=A[i]
        i+=1
    else:
        if num==0:
            ans+=A[i]
            num+=1
        else:
            ans+=A[i]
            i+=1
            num=0
    cnt+=1
print(ans)