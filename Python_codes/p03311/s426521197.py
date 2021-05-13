import statistics
n=int(input())
a=list(map(int,input().split()))
aa=[]
for i in range(n):
    t=a[i]-i-1
    aa.append(t)
aa.sort()
b=statistics.median_high(aa)
ans=0
for i in range(n):
    ans+=abs(aa[i]-b)
print(ans)