n=int(input())
a=list(map(int,input().split()))
m=1000
day_buy=[]
for i in range(n):
    if i==0:
        if a[i]<a[i+1]:
            day_buy.append(i)
    elif i<n-1:
        if a[i-1]>=a[i] and a[i]<a[i+1]:
            day_buy.append(i)
day_sell=[]
for j in range(n):
    if n-1>j>0:
        if a[j-1]<a[j] and a[j]>=a[j+1]:
            day_sell.append(j)
    elif j==n-1>0:
        if a[j-1]<a[j]:
            day_sell.append(j)
k=0
for i in range(len(day_buy)):
    kb=m//a[day_buy[i]]
    m-=kb*a[day_buy[i]]
    k+=kb
    m+=k*a[day_sell[i]]
    k=0
print(m)
