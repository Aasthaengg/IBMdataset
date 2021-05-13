k,n = map(int,input().split())
a = list(map(int,input().split()))
max_lenth = 0

for i in range(1,n):
    lenth = a[i] - a[i-1]
    max_lenth = max(max_lenth, lenth)
else:
    lenth = k - a[-1] + a[0]
    max_lenth = max(max_lenth, lenth)
ans = k - max_lenth
print(ans)