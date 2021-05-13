N,M = map(int, input().split())
A = [[] for i in range(N)]
for i in range(M):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    A[a].append(b)
    A[b].append(a)

if len(A[0])+len(A[-1]) != len(set(A[0]+A[-1])):
        print("POSSIBLE")
else:
    print('IMPOSSIBLE')