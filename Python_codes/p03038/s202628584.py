# 初期入力
#import numpy as np
import sys
input = sys.stdin.readline
N,M = (int(i) for i in input().split())
A = list(map(int, input().split()))
take =[[-1] for i in range(M)]
for x in range(M):
    B,C = (int(i) for i in input().split())
    take[x] =B,C

#
A.sort()
take.sort(key=lambda x: x[1], reverse=True)
take =[(0,0)] +take
ind =[0]*(M+1)
for i in range(1,M+1): #初項に「０」足したから「M]まで
    ind[i] =ind[i-1] +take[i][0]
    if ind[i-1] >=N:
        break
    elif A[ind[i-1]] >=take[i][1]:
        break
    elif ind[i] <N and A[ind[i]] <take[i][1]: #全て一括で置き換える
        A[ind[i-1] :ind[i]] =[take[i][1] ] *(take[i][0]) 
    else:
        for j in range(ind[i-1],ind[i]): #最後は1つずつ確認しながら置き換える
            if N <= j:
                break
            if A[j] <take[i][1]:
                A[j] =take[i][1]
            else:
                break
print(sum(A))