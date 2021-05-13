# B - Shift only
N = int(input())
A = list(map(int,input().split()))

def div2(x):
    ans = 0
    while x%2==0:
        x //= 2
        ans += 1
    return ans

ans = 10000
for a in A:
    ans = min(ans, div2(a))
print(ans)