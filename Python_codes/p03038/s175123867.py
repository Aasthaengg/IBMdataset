N , M = (int(a) for a in input().split())
A = list(map(int,input().split()))
BC = [[int(a) for a in input().split()] for l in range(M)]
A =sorted(A)
BC = sorted(BC , key = lambda x: - x[1])
s = 0

for i in range(N*M) :
    if A[i] < BC[s][1] :
        A[i] = BC[s][1]
    else : break
    BC[s][0] -= 1
    if BC [-1][0] == 0 or i == N-1 :
        break
    if BC[s][0] == 0 :
        s += 1

print(sum(A))



