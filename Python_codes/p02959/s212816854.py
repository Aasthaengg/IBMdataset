import sys
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

b += [0]

ans = 0

for i in range(n+1):
    if a[i] > b[i-1]:
        ans += b[i-1]
        a[i] -= b[i-1]
        b[i-1] = 0
    else:
        ans += a[i]
        b[i-1] -= a[i]
        a[i] = 0
    
    if a[i] > b[i]:
        ans += b[i]
        a[i] -= b[i]
        b[i] = 0
    else:
        ans += a[i]
        b[i] -= a[i]
        a[i] = 0
        
print(ans)