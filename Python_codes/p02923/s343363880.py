n=int(input())
h=list(map(int,input().split()))
ans=0
count=0
hei=h[0]
for i in range(1,n):
    if hei>=h[i]:
        count+=1
    else:
        ans=max(ans,count)
        count=0
    hei=h[i]
print(max(ans,count))