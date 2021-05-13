n,m=map(int,input().split())
num=[]
for i in range(m):
    num.append(list(map(int,input().split())))
num3=[[] for _ in range(n)]
for i in range(m):
    for j in range(1,num[i][0]+1):
        num3[num[i][j]-1].append(i+1)
p=list(map(int,input().split()))
ans=0
for i in range(2**n):
    num2=[0]*m
    num4=0
    for j in range(n):
        if (i>>j) & 1:
            for k in range(len(num3[j])):
                num2[num3[j][k]-1]+=1
    for j in range(m):
        if num2[j]%2!=p[j]:
            num4=1
            break
    if num4==0:
        ans+=1
print(ans)
