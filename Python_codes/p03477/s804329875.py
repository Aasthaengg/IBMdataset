a,b,c,d = list(map(int,input().split()))
L = a+b
R = c+d

if L > R:
    print('Left')
elif L < R:
    print('Right')
else:
    print('Balanced')
