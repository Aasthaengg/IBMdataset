d, n=map(int, input().split())
k=100**d
cnt=0
i=0
while cnt!=n:
    i+=1
    if i%100!=0:
        cnt+=1

print(k*i)