n = int(input())
a = list(map(int, input().split()))
tmp = max(a)
ave = sum(a) / n
ans = 0
for i in range(n):
    if tmp > abs(ave - a[i]):
        ans = i
        tmp = abs(ave - a[i])
print(ans)
