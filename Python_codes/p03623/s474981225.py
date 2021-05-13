x,a,b = map(int,input().split())

s = x-a;t = x-b

if s < 0:
    s = -s
if t < 0:
    t = -t
    
if s > t:
    print('B')
else:
    print('A')