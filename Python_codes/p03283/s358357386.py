N, M, Q = map(int,input().split())
Mlist = []
for i in range(M):
    array = list(map(int, input().strip().split()))
    Mlist.append(array)
Qlist = []
for i in range(Q):
    array = list(map(int, input().strip().split()))
    Qlist.append(array)
p = [[0 for i in range(N)] for j in range(N)]
q = 0
r = [[0 for i in range(N)] for j in range(N)]
def count(k,l):
    s = k
    j = l
    p[s-1][j-1] = p[s-1][j-1] + 1
for i in range(len(Mlist)):
    count(Mlist[i][0],Mlist[i][1])
for i in range(N):
    for j in range(N):
        if i == 0:
            r[i][j] = p[i][j] + r[i][j-1]      
        elif j == 0:
            r[i][j] = p[i][j] +r[i-1][j]
        else:
            r[i][j] = r[i-1][j] + r[i][j-1] - r[i-1][j-1] + p[i][j]
for i in range(len(Qlist)):
    q = 0
    if Qlist[i][0] == 1:
        b = r[Qlist[i][1]-1][Qlist[i][1]-1]
    else:
        b = r[Qlist[i][1]-1][Qlist[i][1]-1] - r[Qlist[i][0]-2][Qlist[i][1]-1]
    print(b)

