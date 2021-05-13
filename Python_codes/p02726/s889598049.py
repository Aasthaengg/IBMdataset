N, X, Y = map(int, input().split())
l = [0] * N
for i in range(1,N):
    for j in range(i+1,N+1):
        #i j
        ij = j - i
        #i x y j
        ixyj = abs(X - i) + 1+ abs(Y -j)
        #i y x j
        iyxj = abs(Y - i) + 1 + abs(X- j)
        length = min(min(ij,ixyj),iyxj)
        l[length] +=1
for i in range(1,N):
    print(l[i])