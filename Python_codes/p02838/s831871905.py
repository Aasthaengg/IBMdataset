n = int(input())
a = list(map(int,input().split()))

c = [0]*100
for i in a:
    b = format(i,'b')[::-1]
    for x in range(len(b)):
        c[x] += int(b[x])

ans = 0
mod = 10**9+7
for i in range(100):
    ans += c[i]*(n-c[i])*2**i
    ans %= mod

print(ans)