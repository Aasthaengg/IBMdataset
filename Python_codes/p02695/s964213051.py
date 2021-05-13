import itertools
n, m, q=map(int, input().split())

l=[[0]*4 for i in range(q)]

for i in range(q):
    l[i][0],l[i][1],l[i][2],l[i][3]=map(int,input().split())

a=[]
for i in range(1,m+1):
    a.append(i)
arr=list(itertools.combinations_with_replacement(a,n))

mx=0
for mask in range(len(arr)):
    tpl=arr[mask]
    ans=0
    for i in range(q):
        if tpl[l[i][1]-1]-tpl[l[i][0]-1]==l[i][2]:
            ans+=l[i][3]
    mx=max(ans,mx)

print(mx)