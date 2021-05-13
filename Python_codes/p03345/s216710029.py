a,b,c,k = map(int,input().split())
if k%2==0:
    res = a-b
else:
    res = b-a
if abs(res) >= 10**18:
    print('Unfair')
else:
    print(res)