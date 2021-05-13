from copy import copy
n=int(input())
a=[0]+list(map(int,input().split()))
ans=[0]*(n+1) 
for i in range(n//2+1,n+1):
    ans[i]=a[i]
for j in reversed(range(1,n//2+1)):
    k=2
    count=0
    j_copy=copy(j)
    a_j=a[j]
    while True:
        count+=ans[k*j_copy]
        k+=1
        if k*j_copy>n:
            break
    if count%2==a_j:
        ans[j]+=0
    else:
        ans[j]+=1
temp=[]
for i in range(1,n+1):
  if ans[i]==1:
    temp.append(str(i))
print(ans.count(1))
print(" ".join(temp))