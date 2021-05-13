n = int(input())

a = list(map(int,input().split()))
total = sum(a)

ans = 10000000000000000000
x = 0
for i in range(n):
    x += a[i]
    if i  < n-1:
        ans = min(ans,abs(total-2*x))

print(ans)  