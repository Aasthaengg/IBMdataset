from sys import stdin, stdout
input = stdin.readline
print = stdout.write

N = int(input())
A = [[int(i) for i in input().split()] for _ in range(N)]
sumA = sum(sum(A, [])) // 2
correct = True

def isCorrect():
    for u in range(N):
        for v in range(u + 1, N):
            for k in range(N):
                if A[u][k] and A[v][k]:
                    #print(u,v,k,A[u][k],A[v][k],A[u][v])
                    if A[u][k] + A[k][v] < A[u][v]:
                        return False
    return True


if not isCorrect(): print(str(-1))
else:
    for u in range(N):
        for v in range(u + 1, N):
            for k in range(N):
                if A[u][k] and A[k][v]:
                    if A[u][k] + A[k][v] == A[u][v]:
                        sumA -= A[u][v]
                        break
    print(str(sumA))
