n=int(input())
ans=[[None]*101 for _ in range(101)] 
a=[[0]*3 for _ in range(n)] 

for i in range(n):
    a[i][0],a[i][1],a[i][2]=map(int,input().split())
a=sorted(a,key=lambda x: x[2],reverse=True)

for i in range(n):
    for cx in range(101):
        for cy in range(101):
            height=a[i][2]+abs(a[i][0]-cx)+abs(a[i][1]-cy)
            if a[i][2]>0:
                if ans[cx][cy]==None or ans[cx][cy]==height:
                    ans[cx][cy]=height
                else:
                    ans[cx][cy]=-1
            else:
                if ans[cx][cy]!=None:
                    if ans[cx][cy]>abs(a[i][0]-cx)+abs(a[i][1]-cy):
                        ans[cx][cy]=-1
                else:
                    ans[a[i][0]][a[i][1]]=-1
        

for cx in range(101):
    for cy in range(101):
        if ans[cx][cy]!=-1:
            if ans[cx][cy]==None: 
                ans[cx][cy]=1
            print(cx,cy,ans[cx][cy])