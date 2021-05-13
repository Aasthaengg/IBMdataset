N,M = map(int, input().split())
A = [map(int,input().split()) for _ in range(M)]
S = []
for i in A:
    for j in i:
        S.append(j)
for i in range(1,N+1):
    print(S.count(i))