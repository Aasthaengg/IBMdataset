import  itertools
n=int(input())
F=[]
for i in range(n):
    a=list(map(int,input().split()))
    F.append(a)
P=[]
for i in range(n):
    a=list(map(int,input().split()))
    P.append(a)

ans=-float("inf")

def j(a):
    tmp=0
    for i in range(n):
        cnt=0
        for j in range(10):
            if F[i][j]==1 and a[j]==1:
                cnt+=1
        tmp+=P[i][cnt]
    return tmp

for pa in itertools.product([0,1],repeat=10):
    pa=list(pa)
    if not pa.count(1)==0:
        ans=max(ans,j(pa))

print(ans)
