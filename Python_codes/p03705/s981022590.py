#AGC015-A
n,a,b = map(int,input().split())

mi = a * (n-2)
ma = b * (n-2)
result = ma - mi + 1
if a > b:
    print(0)
elif n == 1 and a != b:
    print(0)
elif n == 1 and a == b:
    print(1)
    
else:
    print(result)