h,w=map(int,input().split())
a=[input() for _ in range(h)]
d=dict()
for i in range(h):
    for j in range(w):
        if a[i][j] not in d:
            d[a[i][j]]=1
        else:
            d[a[i][j]]+=1
num=[]
for c in d:
    num.append(d[c])
num.sort(reverse=True)
ans=[[0]*w for _ in range(h)]
lis=[]
for i in range(h):
    for j in range(w):
        if ans[i][j]==0:
            if h-1-i==i and w-j-1!=j:
                ans[i][j]=1
                ans[i][w-1-j]=1
                lis.append(2)
            elif h-i-1!=i and w-j-1==j:
                ans[i][j]=1
                ans[h-1-i][j]=1
                lis.append(2)
            elif h-1-i==i and w-j-1==j:
                ans[i][j]=1
                lis.append(1)
            else:
                ans[i][j]=1
                ans[i][w-1-j]=1
                ans[h-1-i][j]=1
                ans[h-1-i][w-1-j]=1
                lis.append(4)
lis.sort(reverse=True)
for i in range(len(num)):
    for j in range(len(lis)):
        if num[i]>=lis[j]:
            num[i]-=lis[j]
            lis[j]=0
if sum(num)!=0 or sum(lis)!=0:
    print("No")
else:
    print("Yes")