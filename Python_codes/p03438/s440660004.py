n=int(input())
*a,=map(int,input().split())
*b,=map(int,input().split())

capacity=0
for i in range(n):
    capacity+=max(0,b[i]-a[i]-(b[i]-a[i])%2)

for i in range(n):
    if a[i]>b[i]:
        capacity-=(a[i]-b[i])*2

if capacity>=0:
    print('Yes')
else:
    print('No')