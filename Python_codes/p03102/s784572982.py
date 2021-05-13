n,m,c=map(int,input().split())
b=[int(i)for i in input().split()]
a=[[int(i)for i in input().split()]for j in range(n)]
res=0
for i in range(n):
    tmp=sum([a[i][j]*b[j]for j in range(m)])+c
    if tmp>0:
        res+=1
print(res)