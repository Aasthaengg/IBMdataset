n, k = map(int, input().split())
a = list(map(int, input().split()))

mod = 10**9 + 7
x = (k*(k+1)//2)%mod
y = (k*(k-1)//2)%mod

r = 0
for i in range(n):
    right = sum(a[i] > j for j in a[i:])
    left = sum(a[i] > j for j in a[:i+1])
    r = (r+((right*x) + (left*y))%mod)%mod
print(r)