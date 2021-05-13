n, k = map(int, input().split())
kk = 0
if n%2 != 0:
    kk = (n+1)//2
else:
    kk = n//2

if k <= kk:
    print("YES")
else:
    print("NO")
