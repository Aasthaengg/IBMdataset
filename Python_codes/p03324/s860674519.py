d, n = map(int, input().split())
if n == 100:
    n += 1
print(n if d==0 else 100*n if d==1 else (100**2)*n)
