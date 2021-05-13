n,m=map(int,input().split())
A=list(map(int,input().split()))
a=sorted(A)
bc=[]
for _ in range(m):
    x=list(map(int,input().split()))
    bc.append(x)
bc.sort(key=lambda x:x[1],reverse=True)
i=0
j=0
k=0
while a[i]<bc[j][1]:
    a[i]=bc[j][1]
    i+=1
    k+=1
    if bc[j][0]==k:
        j+=1
        k=0
    if i>=n or j>=m:
        break
print(sum(a))