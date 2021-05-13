h,w=map(int,input().split())
ans=[]
a=[list(map(int,input().split())) for i in range(h)]
flg=True
for i in range(h):
    if flg:
        for j in range(w):
            if a[i][j]%2==1:
                if j<w-1:
                    a[i][j+1]+=1
                    ans.append((i+1,j+1,i+1,j+2))
                if j==w-1:
                    if i<h-1:
                        a[i+1][j]+=1
                        ans.append((i+1,j+1,i+2,j+1))
        flg=False
    else:
        flg=True
        for j in range(w-1,-1,-1):
            if a[i][j]%2==1:
                if j>0:
                    a[i][j-1]+=1
                    ans.append((i+1,j+1,i+1,j))
                if j==0:
                    if i<h-1:
                        a[i+1][j]+=1
                        ans.append((i+1,j+1,i+2,j+1))
print(len(ans))
for i in ans:
    print(*i)