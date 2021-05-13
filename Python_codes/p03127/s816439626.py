N = int(input())
a = list(map(int, input().split()))
a.sort()

def gcd(a, b):
    if b != 0:
        return gcd(b, a%b)
    else:
        return a
ans = 10**10
for i in range(N-1):
    ans = min(ans, gcd(a[i], a[i+1]))
print(ans)
