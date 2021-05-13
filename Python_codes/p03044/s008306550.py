import sys
sys.setrecursionlimit(10 ** 6)
N = int(input())
uvw = [list(map(int, input().split())) for i in range(N - 1)]
R = [-1] * N
Q = [[] for i in range(N)]
for i in range(N - 1):
    Q[uvw[i][0] - 1].append([uvw[i][1], uvw[i][2]])
    Q[uvw[i][1] - 1].append([uvw[i][0], uvw[i][2]])

def func(i, s, d, l):
    
    if R[i] != -1:
        return

    if R[i] == -1:
        if l %2 == 0:
            R[i] = s
        else:
            R[i] = d
            tmp = s
            s = d
            d = tmp
    for j in range(len(Q[i])):
        func(Q[i][j][0] - 1, s, d, Q[i][j][1])

func(uvw[0][0] - 1, 0, 1, 0)
for i in range(len(R)):
    print(R[i])