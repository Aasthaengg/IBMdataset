s = int(input())
a = [0]*(s+5)
a[0] = 1
mod = 10**9 + 7
for i in range(3 , s+1):
    if i < 3 :
        continue

    a[i] = (a[i-1] + a[i-3]) % mod

print(a[s])