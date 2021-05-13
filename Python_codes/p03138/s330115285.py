n , k = map(int,input().split())
a = list(map(int,input().split()))
bi = [0 for i in range(41)]
if n % 2 == 0:
    kahan = n//2-1
elif n % 2 == 1:
    kahan = n//2
for i in range(n):
    for j in range(41):
        bi[j] += (a[i] >> j) & 1

for i in reversed(range(41)):
    if k < pow(2,i):
        continue
    elif k >= pow(2,i):
        if bi[i] <= kahan:
            bi[i] = n - bi[i]
            k -= pow(2,i)
ans = 0
for i in range(41):
    ans += bi[i]*pow(2,i)

print(ans)