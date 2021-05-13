n = int(input())
a = list(map(int,input().split()))
k = 1000
s = 0
for i in range(n-1):
    if s == 0:
        if a[i] < a[i+1]:
            s = k // a[i]
            k -= s * a[i]
    else:
        if a[i] > a[i+1]:
            k += s * a[i]
            s = 0
print(k + s * a[-1])