n , x = map(int, input().split())
a = list(map(int,input().split()))
a2 =[0]*n
for i in range(n):
    if a[i]>x:
        a2[i]=x
    else:
        a2[i] = a[i]
s = 0
for i in range(n-1):
    if a2[i]+a2[i+1]>x:
        a2[i+1]=x-a2[i]
for i in range(n):
    s+=a[i]-a2[i]
print(s)
