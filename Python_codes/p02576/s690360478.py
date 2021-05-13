n, x, t = [int(i) for i in input().split()]
amari = n%x
syou  = int((n-amari)/x)
if amari==0:
    print(t*syou)
else:
    print(t*(syou+1))