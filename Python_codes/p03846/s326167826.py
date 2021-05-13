n = int(input())
a = list(map(int,input().split()))
a.sort()

mod = 10**9+7
ans = 1

if n % 2 == 0:
    for i in range(n):
        if i % 2 == 0:
            if a[i] != i + 1:
                ans = 0
        else:
            if a[i] != i:
                ans = 0
else:
    for i in range(n):
        if i % 2 == 0:
            if a[i] != i:
                ans = 0
        else:
            if a[i] != i + 1:
                ans = 0

for i in range(n//2):
    ans *= 2
    ans %= mod

print(ans)
