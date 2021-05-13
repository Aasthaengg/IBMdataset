from collections import deque

N,M=map(int,input().split())

#S = [[0 for j in range(3)] for i in range(2)]　2行3列の場合
S = [[]for i in range(N+1)]
deq=deque()

for i in range(M):
    A,B=map(int,input().split())
    S[A].append(B)
    S[B].append(A)
    
#print(S)    
lenN=len(S[N])
for i in range(lenN):
    v=S[N][i]
    #print(v)
    #print(S[v])
    
    if 1 in S[v]: 
        print("POSSIBLE")
        exit()

print("IMPOSSIBLE")        