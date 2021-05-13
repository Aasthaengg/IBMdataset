N,K = map(int, input().split())
A = list(map(int, input().split()))

move = 1
l = [1]
flag = [False]*(N+1)
flag[1] = True

for i in range(K):
    move = A[move-1]
    if flag[move]:
        break
    flag[move] = True
    l.append(move)

ind = l.index(move)
rest = (K-ind) % (len(l) - ind) + ind

print(l[rest])
