N, x = map(int,input().split())
a = list(map(int,input().split()))

left = 0
total = 0
for i in range(N):
    cnt = max(a[i]-(x-left),0)
    total += cnt
    left = a[i]-cnt
print(total)

