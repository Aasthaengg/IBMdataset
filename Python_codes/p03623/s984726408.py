x,a,b = (int(i) for i in input().split())

A  = abs(x - a)
B  = abs(x - b)

if A > B :
    print('B')
else:
    print('A')
