n=int(input())
p=list(map(int,input().split()))
count=0
for i in range(1,n-1):
    a=[p[i-1],p[i],p[i+1]]
    if p[i]!=min(a) and p[i]!=max(a):
        count+=1
print(count)
