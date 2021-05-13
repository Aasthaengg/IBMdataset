N = int(input())
T = list(map(int,input().split()))
T.insert(0,0)
M = int(input())
X = [list(map(int,input().split())) for _ in range(M)] 
tot = sum(T)
for i in range(M):
    p,x = X[i]
    print(tot-T[p]+x)