N = int(input())
A = [[0 for _ in range(N+1)]]
for _ in range(N):
    a = list(map(int,input().split()))
    a.insert(0,0)
    A.append(a)
tot = 0
for i in range(1,N):
    for j in range(i,N+1):
        tot += A[i][j]
for i in range(1,N):
    for j in range(i+1,N+1):
        for k in range(1,N+1):
            if k!=i and k!=j:
                if A[i][j]>A[i][k]+A[k][j]:
                    tot = -1
                    break
                elif A[i][j]==A[i][k]+A[k][j]:
                    tot -= A[i][j]
                    break
        if tot<0:break
    if tot<0:break
print(tot)