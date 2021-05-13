n = int(input())
a = list(map(int,input().split()))
mi = float('INF')
t=0
for i in range(n):
    if abs(a[i])<mi:
        mi=abs(a[i])
        t=i
a1=a.copy()
sum1=0
for i in range(n-2):
    if a1[i]<0:
        sum1+=a1[i]*(-1)
        a1[i+1]*=-1
    else:
        sum1+=a1[i]
if a1[n-2]+a1[n-1]>(a1[n-2]+a1[n-1])*(-1):
    sum1+=a1[n-2]+a1[n-1]
else:
    sum1+=(a1[n-2]+a1[n-1])*(-1)

sum2=0
for i in range(n-2):
    if i==t and a[i]<0:
        sum2+=a[i]
        continue
    elif i==t and a[i]>0:
        sum2-=a[i]
        a[i+1]*=-1
        continue
    if a[i]<0:
        sum2+=a[i]*(-1)
        a[i+1]*=-1
    else:
        sum2+=a[i]
if a[n-2]+a[n-1]>(a[n-2]+a[n-1])*(-1):
    sum2+=a[n-2]+a[n-1]
else:
    sum2+=(a[n-2]+a[n-1])*(-1)
print(max(sum1,sum2))
