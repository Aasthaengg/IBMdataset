n, p = map(int,input().split())
s = str(input())
ans = 0

if p == 2 or p == 5:
    for i in range(n):
        if int(s[i])%p == 0:
            ans += i+1
    print(ans)
    exit()

tmp = [0] * p
tmp[0] = 1
mod = 0
r = 1
for i in range(1,n+1):
    mod += (int(s[-i]) * r) % p
    mod %= p
    tmp[mod] += 1
    r *= 10
    r %= p

for i in tmp:
    ans += i*(i-1)//2

print(ans)