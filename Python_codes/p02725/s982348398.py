k,n = map(int,input().split())
a = list(map(int,input().split()))
max_len = k - a[n-1] + a[0]
for i in range(2, n):
    if a[i]-a[i-1] > max_len:
        max_len = a[i]-a[i-1]

print(k - max_len)