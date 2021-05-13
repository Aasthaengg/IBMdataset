N,x=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
count=0
for i in range(N):
    if x<a[i]:
        break
    elif x==a[i] or i<N-1:
        count+=1
        x-=a[i]


print(count)
