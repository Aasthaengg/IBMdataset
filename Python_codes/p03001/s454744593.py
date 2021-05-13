W,H,x,y = (int(x) for x in input().split())
MAX = (W*H)/2
if 2*x==W and 2*y==H:
    print('{} 1'.format(MAX))
else:
    print('{} 0'.format(MAX))