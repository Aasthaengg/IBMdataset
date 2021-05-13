n = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
c = a[0]
ch = -(-a[0]//2)
minD = 10**9
x = -1
for i in range(n):
    dif = abs(a[i]-ch)
    if minD>=dif:
        minD=dif
        x = a[i]
print(c,x)