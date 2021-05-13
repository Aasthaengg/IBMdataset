n = int(input())
a = list(map(int,input().split()))
sum = sum(a)
min = 10000000
ans = 0
for i in range(n):
    if abs(sum - (a[i] * n)) < min:
        min = abs(sum - (a[i] * n))
        ans = i
print(ans)