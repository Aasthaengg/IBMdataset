n,m=map(int,input().split())
x=int(input())
l=[int(i) for i in input().split()]
mat=[[0 for j in range(m)]for i in range(n)]
curr=1 
c=0 
j1=0
for i in range(n): 
    for j in range(m):
        mat[i][j]=curr 
        c+=1 
        if c==l[j1]: 
            curr+=1 
            j1+=1
            c=0 
for i in range(n):
    if i&1:
        mat[i]=mat[i][::-1]
for i in range(n):
    print(*mat[i])