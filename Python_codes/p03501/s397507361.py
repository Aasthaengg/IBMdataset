n,a,b = map(int, input().split())

if a*n >= b:
    print(b)
    exit()
if a*n <= b:
    print(a*n)