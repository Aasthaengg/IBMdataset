(N,M,Q) = map(int,input().split())
Qs = []
for i in range(Q):
    Qs.append(list(map(int,input().split())))
A = [1]*N
score = 0
while(1):
    if A[0]>M:
        break
    current_score = 0
    for i in range(Q):
        if A[Qs[i][1]-1]-A[Qs[i][0]-1] == Qs[i][2]:
            current_score += Qs[i][3]
    score = max(score,current_score)
    for i in range(1,N):
        if A[i]== M:
            A[i-1] += 1
            for j in range(i,N):
                A[j] = A[i-1]
            break
        if i == N-1:
            A[N-1] += 1
print(score)
