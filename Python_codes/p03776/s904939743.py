nCk = [[0 for i in range(51)] for j in range(51)]

nCk[1][0] = 1
nCk[1][1] = 1
for i in range(2, 51):
    for j in range(51):
        if j > 0:
            nCk[i][j] = nCk[i-1][j-1] + nCk[i-1][j]
        else:
            nCk[i][j] = nCk[i-1][j]

N, A, B = map(int,input().split())
kouho = []
V = list(map(int,input().split()))
V.sort(reverse = True)
acc = 0
for i in range(B):
    if i < A-1:
        acc += V[i]
    else:
        acc += V[i]
        kouho.append(acc / (i+1))

print(str(kouho[0]))

cnt = 0
for i in range(len(kouho)):
    m = 0
    n = 0
    if kouho[i] != kouho[0]:
        break
    for j in range(N):
        if V[j] == V[A+i-1]:
            if j < A+i:
                m+=1
            n+=1
    cnt += nCk[n][m]
print(str(cnt))