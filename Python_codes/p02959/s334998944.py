n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

c = 0
for i in range(n):
    if b[i] < a[i]:
        c += b[i]
    else:
        d = min(a[i+1],b[i]-a[i])
        a[i+1] -=d
        c += a[i]+d
print(c)