n, m, l = (int(i) for i in input().split())
A = []
B = []
#C = [[0] * n] * l
C = [[0 for i in range(l)] for j in range(n)]

#??\?????????????????????????´?
for i in range(n):
    #swap_list = input().split()
    #A.append(swap_list)
    A.append([int(i) for i in input().split()])
for i in range(m):
    #swap_list = input().split()
    #B.append(swap_list)
    B.append([int(i) for i in input().split()])
#????????????????¨????
for i in range(n):
    for j in range(l):
        for k in range(m):
            C[i][j] += A[i][k] * B[k][j]
#?????????????????????
#for i in range(n):
#    for j in range(l):
#        print("{0}".format(C[i][j]), end="\b")
#    print("")
#for i in range(n):
#    print(" ".join(map(str, C[i][:])))
for r in C:
    print(" ".join([str(d) for d in r]))