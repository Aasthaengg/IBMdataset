import math , sys

N , M = list(map(int, input().split()))
H = list(map(int, input().split()))
Es = [[] for _ in range(N)]
for i in range(M):
    A , B = list(map(int, input().split()))
    A -=1 ; B-=1
    Es[A].append(B)
    Es[B].append(A)
ans = 0
for i in range(N):
    Es[i] = list(set(Es[i]))
for i in range(N):
    if len(Es[i]) == 0:
        ans+=1
    else:
        Max = max( [ H[Es[i][j]] for j in range( len(Es[i]) ) ] )
        if H[i] > Max:
            ans+=1
print(ans)