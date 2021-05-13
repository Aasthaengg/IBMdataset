n,k=map(int,input().split())
l=list(map(int,input().split()))
l1=[0]*(k+1)
l1[0]=2
for i in l:
    l1[i]=1
for i in range(1,k+1):
    if l1[i]==0:
        for j in l:
            if l1[i-j]==2 and i-j>=0:
                l1[i]=1
                break
            else:
                l1[i]=2
if l1[k]==1:
    print("First")
else:
    print("Second")
