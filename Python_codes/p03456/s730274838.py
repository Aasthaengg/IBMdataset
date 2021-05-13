a, b = input().split()
n = int(a+b)
if round(n**0.5)**2==n:
    print('Yes')
else:
    print('No')