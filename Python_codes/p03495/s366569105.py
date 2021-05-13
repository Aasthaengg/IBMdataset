n,k=map(int,input().split())
a=list(map(int,input().split()))

d=[0]*n
for i in range(n):
    d[a[i]-1]+=1

d.sort(reverse=True)

sm=0
for i in range(k):
    if i>=n:
        break
    sm+=d[i]

print(n-sm)    