n=int(input())
h=list(map(int,input().split()))
ans=0
for i in range(1,max(h)+1):
    num=0
    for j in range(n):
        if num==0 and h[j]>=i:
            ans+=1
            num=1
        if num==1 and h[j]<i:
            num=0
print(ans)
