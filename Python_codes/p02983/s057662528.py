l,r=map(int, input().split())
mo=2019
ans=2018
r=min(r, l+mo-1)
#max in k~k+2019 line seg. i<k+2019 and k<j
for i in range(l,r):
    for j in range(i+1,r+1):
        tmp=i*j
        ans=min(ans,tmp%mo)
print(ans)