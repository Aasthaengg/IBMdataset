n, m = map(int, input().split())
a = list (map(int, input().split()))

b = 0

for i in range(m):
    b = b + a[i]

if n >= b:
    print( n - b )

if n < b:
    print( -1 )