import math
K = int(input())
A = list(map(int,input().split()))
a = 1
L,S = 2,2 

while a <= K:
    if math.ceil(S/A[-a])*A[-a] < S or L < math.ceil(S/A[-a])*A[-a]:
        print('-1')
        exit()
    S = math.ceil(S/A[-a])*A[-a]
    L = math.floor(L/A[-a])*A[-a] + A[-a] -1
    a += 1
print(S,L)

    
