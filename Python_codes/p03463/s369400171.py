N,A,B = [int(i) for i in input().split()]

if abs(B-A)%2 != 0:
    print('Borys')
else:
    print('Alice')
