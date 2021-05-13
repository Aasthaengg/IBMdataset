n,m,x=map(int,input().split())
a=list(map(int,input().split()))

count_a=0
for i in range(m):
    if a[i]<x:
        count_a+=1

count_b=m-count_a

print(min(count_a,count_b))