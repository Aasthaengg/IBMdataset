n = int(input())
a = list(map(int,input().split()))
a = sorted(a)
x = a[-1]/2
ans = 0
dis = float("Inf")
for i in range(n-1):
    if dis > abs(x-a[i]):
        ans = a[i]
        dis = abs(x-a[i])
print(a[-1],ans)