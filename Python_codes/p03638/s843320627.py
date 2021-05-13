h,w = map(int,input().split())
n = int(input())
ai = [int(i) for i in input().split()]

cij = [[0 for i in range(w)] for j in range(h)]

aij = []

for i in range(n):
    for j in range(ai[i]):
        aij.append(i+1)

for i in range(h):
    #print(i)
    if i % 2 == 0:
        for j in range(w):
            cij[i][j] = aij[i*w+j]
            #print(cij)
    else:
        for j in range(w):
            #print(cij[i][w-1-j],i*w+j)
            cij[i][w-1-j] = aij[i*w+j]

for i in range(h):
    print(*cij[i])

