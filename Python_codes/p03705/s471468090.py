n,a,b = list(map(int, input().split()))
if n == 1:
    if a==b:
        print(1)
    else:
        print(0)
elif a>b:
    print(0)
else:
    MIN = a * (n-1) + b
    MAX = a * 1 + b * (n-1)
    print(MAX-MIN+1)