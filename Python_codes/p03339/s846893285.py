import numpy as np
N = int(input())
S = "d"+input()+"d"

#index=0,N+1は初期化に必要
leftwest = np.array([0]*(N+2))
righteast = np.array([0]*(N+2))

for i in range(1,N+1):
    if S[i] == "W":
        leftwest[i+1] = leftwest[i] + 1
    else:
        leftwest[i+1] = leftwest[i]
        
    if S[-(i+1)] == "E":
        righteast[-(i+2)] = righteast[-(i+1)] + 1
    else:
        righteast[-(i+2)] = righteast[-(i+1)]

#print("left",leftwest)
#print('right',righteast)


print(min(leftwest[1:N+1]+righteast[1:N+1]))