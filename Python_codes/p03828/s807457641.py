n = int(input())
ans = 1
a = [0 for i in range(n+1)]
for k in range(1,n+1):
    i = k
    while i % 2 == 0:
        a[2] += 1
        i //= 2
    j = 3
    while j ** 2 <= i:
        if i % j == 0:
            a[j] += 1
            i //= j
        else:
            j+=2
    if i != 1:
        a[i]+=1
for i in a:
    if i != 0:
        ans *= (i+1)
        ans %= (10**9+7)
print(ans)