n,m,k=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
tot_a=0
tot_b=0
#Aだけでどこまでいけるか
a=[0]
b=[0]
for i in range(n):
    a.append(a[-1]+A[i])
for j in range(m):
    b.append(b[-1]+B[j])
#print(a,b)
ans=0
j=m
for i in range(n+1):
    if a[i]>k:
        break
    while a[i]+b[j]>k:
        j-=1
    ans=max(ans,i+j)
print(ans)