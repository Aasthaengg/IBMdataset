n=int(input())
a=[int(i) for i in input().split()]
takasa=0

for i in range(n-1):
    if a[i]>a[i+1]:
        takasa+=a[i]-a[i+1]
        a[i+1]+=a[i]-a[i+1]
print(takasa)