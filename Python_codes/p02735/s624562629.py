h,w=map(int,input().split())
s=[]
for _ in range(h):
    s.append(list(input()))
a=[[0]]
for i in range(1,h):
    t=a[i-1][0]
    if s[i][0]!=s[i-1][0]:
        a.append([t+1])
    else:
        a.append([t])

for j in range(1,w):
    t=a[0][j-1]
    if s[0][j]!=s[0][j-1]:
        a[0].append(t+1)
    else:
        a[0].append(t)

for i in range(1,h):
    for j in range(1,w):
        up=a[i-1][j]
        left=a[i][j-1]
        if s[i][j]!=s[i-1][j]:
            up += 1
        if s[i][j]!=s[i][j-1]:
            left += 1
        mn=min(up,left)
        a[i].append(mn)
num=a[h-1][w-1]
ans=(num+1)//2
if s[0][0]=='#' and num%2==0:
    ans += 1
print(ans)