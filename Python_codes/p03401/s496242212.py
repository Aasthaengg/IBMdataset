n=int(input())
a=[0]+list(map(int,input().split()))+[0]

dis=0
d=[0]*n

for i in range(1,n+1):
    dis+=abs(a[i]-a[i-1])
    if a[i+1]<a[i] and a[i-1]<a[i]:
        d[i-1]=2*(a[i]-max(a[i-1],a[i+1]))
    if a[i+1]>a[i] and a[i-1]>a[i]:
        d[i-1]=2*(min(a[i-1],a[i+1])-a[i])
dis+=abs(a[n+1]-a[n])

for i in range(n):
    print(dis-d[i])