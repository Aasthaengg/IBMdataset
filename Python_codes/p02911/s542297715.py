n,k,q=map(int,input().split())
a=[]
for i in range(q):
    a.append(int(input()))
ans=[-1]+[0]*n

for i in range(q):
    ans[a[i]]+=1

for i in range(1,n+1):
    if k-(q-ans[i])>0:
        print('Yes')
    else:
        print('No')
