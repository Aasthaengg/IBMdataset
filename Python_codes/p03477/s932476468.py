A,B,C,D = (int(i) for i in input().split())

x = A + B
y = C + D

if x > y:
    print('Left')
elif x < y:
    print('Right')
else:
    print('Balanced')