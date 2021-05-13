n, k = map(int, input().split())
M = 10**9 + 7

def f(a,b):
    return (a+b)*(b-a+1)//2

ans = 0
for s in range(k, n+2):
    l = f(0,s-1) % M
    r = f(n-s+1,n) % M
    ans += r-l+1

print(ans%M)
