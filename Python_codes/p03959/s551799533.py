import sys
n = int(input())
t = list(map(int, input().split()))
a = list(map(int, input().split()))

h = [min(t[i],a[i]) for i in range(n)]
fixed = [False] * n
fixed[0] = True; fixed[n-1] = True

if a[n-1] > t[n-1] or t[0] > a[0]:
    print(0)
    sys.exit(0)
# takahashi check
for i in range(1,n):
    if t[i] > t[i-1]: 
        fixed[i] = True
        if t[i] > a[i]:
            print(0)
            sys.exit(0)
# aoki check
for i in range(n-2, -1, -1):
    if a[i] > a[i+1]:
        fixed[i] = True
        if a[i] > t[i]:
            print(0)
            sys.exit(0)

# calc ans
ans = 1
for i in range(n):
    if not fixed[i]:
        ans = ans * h[i] % (10**9+7)
print(ans)