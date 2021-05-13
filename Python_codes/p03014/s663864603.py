h,w=map(int,input().split())
s=[list(input()) for _ in range(h)]
left=[[0]*w for _ in range(h)]
right=[[0]*w for _ in range(h)]
up=[[0]*w for _ in range(h)]
down=[[0]*w for _ in range(h)]
for i in range(h):
    temp=1
    for j in range(w):
        if s[i][j]==".":
            left[i][j]+=temp
            temp+=1
        else:
            temp=1
for i in range(h):
    temp=1
    for j in range(w)[::-1]:
        if s[i][j]==".":
            right[i][j]+=temp
            temp+=1
        else:
            temp=1
for i in range(w):
    temp=1
    for j in range(h):
        if s[j][i]==".":
            down[j][i]+=temp
            temp+=1
        else:
            temp=1
for i in range(w):
    temp=1
    for j in range(h)[::-1]:
        if s[j][i]==".":
            up[j][i]+=temp
            temp+=1
        else:
            temp=1
ans=1
for i in range(h):
    for j in range(w):
        ans=max(ans,up[i][j]+down[i][j]+left[i][j]+right[i][j]-3)
print(ans)