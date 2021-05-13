a,b = map(int,input().split())
if not a%3 or not b%3 or not (a+b)%3:
    print('Possible')
else:
    print('Impossible')