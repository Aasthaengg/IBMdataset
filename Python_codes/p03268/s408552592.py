# 2019/09/10
# かんにんぐ

n,k=map(int,input().split())
cnt=0
num=[0]*(k+1)
for i in range(1,n+1):
    num[i%k]+=1

for a in range(k):
    b=(k-a)%k
    c=(k-a)%k
    if (b+c)%k:continue
    cnt+=num[a]*num[b]*num[c]
    
print(cnt)
