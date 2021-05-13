
N = int(raw_input())

if N == 3:
    print 2
    print 1, 3
    print 2, 3

elif N & 1:
    a = 0
    for i in range(1, N ):
        for j in range(i + 1, N):
            if i != N - j:
                a += 1
    
    for i in range(1, N):
        a += 1


    print a
    for i in range(1, N ):
        for j in range(i + 1, N):
            if i != N - j:
                print i, j
    
    for i in range(1, N):
        print i, N

else:
    a = 0
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if i != N - j + 1:
                a += 1

    print a
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if i != N - j + 1:
                a += 1
                print i, j
    
