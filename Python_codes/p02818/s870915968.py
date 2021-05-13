a, b, k = map(int,input().split())

if a > k:
    a -= k
elif b > k-a:
    k -= a
    a = 0
    b -= k
else:
    a, b = 0,0

print(a,b)
