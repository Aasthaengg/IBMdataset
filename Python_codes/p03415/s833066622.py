def actual(C):
    return C[0][0] + C[1][1] + C[2][2]
    # return ''.join((C[i][j] for i, j in zip(range(len(C)), range(len(C)))))

C = []
C.append(input())
C.append(input())
C.append(input())

print(actual(C))
