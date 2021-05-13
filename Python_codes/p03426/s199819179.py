h,w,d=map(int,input().split())
A=[]
for _ in range(h):
    A.append([int(i) for i in input().split()])
q=int(input())
lr=[]
for _ in range(q):
    l,r = map(int,input().split())
    lr.append((l,r))
D=dict()
for i in range(h):
    for j in range(w):
        D[A[i][j]]=(i,j)

def dist(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])
#ans=[[-1 for _ in range(h*w//d+1)] for _ in range(d)]
res=dict()
for i in range(d):
    j=i+1
    cnt=0
    res[j]=0
    #ans[i][0] = 0
    while j<=h*w-d:
        #ans[i][cnt+1] = ans[i][cnt] + dist(D[j],D[j+d])
        res[j+d] = res[j]+dist(D[j],D[j+d]) #ans[i][cnt]
        j+=d
        cnt+=1
for l,r in lr:
    print(res[r]-res[l])