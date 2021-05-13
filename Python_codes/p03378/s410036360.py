N,M,X = map(int,input().split())
A = list(map(int,input().split()))
c = 0
d = 0
for i in range(1,X):
    if i in A:
        c += 1
for j in range(X+1,N):
    if j in A:
        d += 1
        
print(min(c,d))

