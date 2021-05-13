mtx = [list(map(int, input().split())) for _ in range(3)]

diff1 = mtx[0][0] - mtx[1][0]
diff2 = mtx[0][0] - mtx[2][0]

diff3 = mtx[0][0] - mtx[0][1]
diff4 = mtx[0][0] - mtx[0][2]

if mtx[0][1] - mtx[1][1] != diff1:
    print('No')
elif mtx[0][2] - mtx[1][2] != diff1:
    print('No')
elif mtx[0][1] - mtx[2][1] != diff2:
    print('No')
elif mtx[0][2] - mtx[2][2] != diff2:
    print('No')
elif mtx[1][0] - mtx[1][1] != diff3:
    print('No')
elif mtx[2][0] - mtx[2][1] != diff3:
    print('No')
elif mtx[1][0] - mtx[1][2] != diff4:
    print('No')
elif mtx[2][0] - mtx[2][2] != diff4:
    print('No')
else:
    print('Yes')
