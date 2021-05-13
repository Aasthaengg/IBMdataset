from operator import itemgetter
N = int(input())
R = [list(input().split()) for i in range(N)]
R = [(R[i][0], int(R[i][1]), i+1) for i in range(N)]
S = sorted(R, key=itemgetter(1), reverse=True)
T = sorted(S, key=itemgetter(0))
for t in T:
    print(t[2])
