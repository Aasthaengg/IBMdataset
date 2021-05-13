n = int(input())
a = list(map(int,input().split()))

a.sort()
k = a[n-1]
r = a[0]
dis = abs(a[n-1]/2-a[0])
for i in range(n-1):
    if dis > abs(a[n-1]/2-a[i]):
        dis = abs(a[n-1]/2-a[i])
        r = a[i]
print(k,r)

