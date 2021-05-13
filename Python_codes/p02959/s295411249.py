n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

cnt = 0
for i in range(n-1, -1, -1):
    cnt += min(b[i], a[i]+a[i+1])
    diff = b[i] - a[i+1]
    if diff > 0:
        a[i] = max(0, a[i]-diff)

print(cnt)