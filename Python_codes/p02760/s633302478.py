import numpy
A1 = numpy.array(list(map(int, input().split())))
A2 = numpy.array(list(map(int, input().split())))
A3 = numpy.array(list(map(int, input().split())))

A = numpy.array([A1, A2, A3])
C = numpy.zeros(A.shape)

N = int(input())
B = []
for _ in range(N):
    b = int(input())
    B.append(b)

    C[A == b] = 1

diag1 = numpy.array([C[0,0], C[1,1], C[2,2]])
diag2 = numpy.array([C[0,2], C[1,1], C[2,0]])

flag = False

if numpy.all(C[0] == 1) or numpy.all(C[1] == 1) or numpy.all(C[2] == 1):
    flag = True

if numpy.all(C.T[0] == 1) or numpy.all(C.T[1] == 1) or numpy.all(C.T[2] == 1):
    flag = True

if numpy.all(diag1 == 1) or numpy.all(diag2 == 1):
    flag = True

if flag:
    print('Yes')
else:
    print('No')