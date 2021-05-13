import numpy as np
import sys

input=sys.stdin.readline

n,m,q = list(map(int, input().split()))

lrs = [list(map(int, input().split())) for _ in range(m)]
pqs = [list(map(int, input().split())) for _ in range(q)]

train_array = np.zeros((n+1,n+1),dtype=int)

for lr in lrs:
    train_array[lr[0]][lr[1]] +=1


#print(train_array)

train_array_ruisekiwa = np.zeros((n+1,n+1), dtype = int)

for i in range(1, n+1):
    for j in range(1, n+1):
        train_array_ruisekiwa[i][j] = train_array[i][j] + train_array_ruisekiwa[i][j-1] + train_array_ruisekiwa[i-1][j] - train_array_ruisekiwa[i-1][j-1]

#print(train_array_ruisekiwa)

for pq in pqs:
    print(train_array_ruisekiwa[pq[1]][pq[1]] - train_array_ruisekiwa[pq[1]][pq[0]-1] - train_array_ruisekiwa[pq[0]-1][pq[1]] + train_array_ruisekiwa[pq[0]-1][pq[0]-1])

