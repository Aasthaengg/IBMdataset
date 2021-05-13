N, M = map(int,input().split())

L = 0
R = N+1
for _ in range(M):
    l,r = map(int,input().split())
    
    L = max(l,L)
    R = min(r,R)

print(len(range(L,R+1)))