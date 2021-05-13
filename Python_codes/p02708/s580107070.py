n, k = map(int, input().split())

ans = 0

def select(l, r):
    return (l+r)*(r-l+1) // 2

for i in range(k, n+2):
    l = select(0, i-1)
    r = select(n-i+1, n)
    ans += (r-l+1) 
    ans %= (pow(10, 9) + 7)

print(ans)