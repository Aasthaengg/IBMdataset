N=int(input())
*H,=map(int,input().split())

ans=0
M=max(H)
count=0
while count<=M:
    if H[0]>=count:
        ans+=1
    i=1
    while i<N:
        if H[i]>=count and H[i-1]<count:
            ans+=1
        i+=1
    count+=1

print(ans-1)