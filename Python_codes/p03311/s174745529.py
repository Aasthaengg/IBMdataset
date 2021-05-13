n = int(input())
a = [int(x) for x in input().split()]
for i in range(1, n+1):
    a[i-1] -= i 
a.sort()
b = n // 2
if n % 2 == 1:
    b = a[n//2]
else:
    b = (a[n//2] + a[n//2 - 1])//2
ans = 0
for x in a:
    ans += abs(x - b)
print(ans)