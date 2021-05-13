a,b,c,k = map(int,input().split())

lim = 10**18
_a = b+c
_b = a+c
if lim < _a-_b:
    print('Unfair')
elif k%2==0:
    print((_a-_b)*-1)
else:
    print(_a-_b)