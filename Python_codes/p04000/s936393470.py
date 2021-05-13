h,w,n=map(int,input().split())
s=set()
l=[[0,0],[1,1],[1,-1],[-1,1],[-1,-1],[0,1],[0,-1],[1,0],[-1,0]]
ans=[(h-2)*(w-2),0,0,0,0,0,0,0,0,0]
for i in range(n):
    a,b=[int(j) for j in input().split()]
    s.add((a,b))
    for i,j in l:
        if a+i>=1 and a+i<=h and b+j>=1 and b+j<=w:
            c=0
            for p,q in l:
                if a+i+p>=1 and a+i+p<=h and b+j+q>=1 and b+j+q<=w:
                    if (a+i+p,b+j+q) in s:
                        c+=1
                else:
                    c=0
                    break
            if c!=0:
                ans[c-1]-=1
                ans[c]+=1

for i in range(10):
    print(ans[i])





