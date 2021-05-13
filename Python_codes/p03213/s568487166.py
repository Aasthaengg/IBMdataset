n=int(input())

l=[0]*(n+1)
p=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
for i in p:
    temp=n
    while temp>=i:
        temp//=i
        l[i]+=temp
var=sorted([g for g in l if g])
ans=sum(int(x>=74)for x in var)
lo=len(var)
for a,b in [(3,25),(5,15)]:
    for i in range(lo):
        for j in range(lo):
            if i!=j and a-1<=var[i]and b-1<=var[j]:
                ans+=1
for i in range(lo):
    for j in range(lo):
        for k in range(j+1,lo):
            if i!=j and k!=i and var[i]>=2 and var[j]>=4 and var[k]>=4:
                ans+=1
print(ans)
