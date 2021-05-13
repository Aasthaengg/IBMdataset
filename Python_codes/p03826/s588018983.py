A, B, C, D = map(int,input().split())

volume1 = A * B
volume2 = C * D

if volume1 > volume2:
    print(volume1)
else:
    print(volume2)