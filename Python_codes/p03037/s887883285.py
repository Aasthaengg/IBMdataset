
N, M = map(int, input().split())

L = [0] * M
R = [0] * M


LR = [0] * M
for i in range(M):
    L[i], R[i] = map(int, input().split())

ans = min(R) - max(L) 
if ans >=0:
    print(ans + 1)
    
else:
    print(0)
    
#print(max(L))
#print(min(R))