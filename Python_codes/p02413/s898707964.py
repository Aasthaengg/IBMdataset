r, c = map(int, input().split())
M, C = [list(map(int, input().split())) for i in range(r)], [0 for j in range(c)]
for i in range(r):
    for j in range(c):
        C[j] += M[i][j]
        print('%d' %(M[i][j]), end=' ')
    print(sum(M[i]))
for j in range(c):
    print('%d' %(C[j]), end=' ')
print(sum(C))