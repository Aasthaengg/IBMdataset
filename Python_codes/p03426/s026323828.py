H,W,D=map(int,input().split())
A=[]
for i in range(H):
    a=list(map(int,input().split()))
    A.append(a)
Q=int(input())
L=[]
R=[]

lst=[[]for _ in range(H*W)]
for i in range(H):
    for j in range(W):
        lst[A[i][j]-1].append(i)
        lst[A[i][j]-1].append(j)
#print(lst)
#print(lst[1][1])
d=[]
for i in range(D):
    cnt=[0]
    for j in range(i+D,H*W,D):
        cnt.append(cnt[-1]+abs(lst[j][0]-lst[j-D][0])+abs(lst[j][1]-lst[j-D][1]))
    d.append(cnt)
ans=[]
#print(cnt)
#print(d)
for i in range(Q):
    l,r=map(int,input().split())
    ll=(l-1)%D
    count=d[ll]
    r-=1
    l-=1
    #print(count)
    vall=count[l//D]
    #print(l//D)
    #print(r//D)
    valr=count[r//D]
    val=valr-vall
    #print(val)
    ans.append(val)

for i in range(Q):
    print(ans[i])