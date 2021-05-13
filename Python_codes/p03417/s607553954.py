n, m = map(int,input().split())
if m >= 3 and n >= 3:
    print((m-2) * (n-2))
elif (m == 2 or n == 2):
    print(0)
elif m >= 3 or n >= 3:
    print((max(m,n)-2) * min(m,n))
else:
    if (m * n) % 2 == 0:
        print(0)
    else:
        print(m * n)