from operator import itemgetter
N = int(input())

T = list()
for i in range(N):
    S, P = map(str, input().split())
    T.append((S, int(P), str(i+1)))

T = sorted(T, key=itemgetter(1), reverse=True)
T = sorted(T, key=itemgetter(0))
for t in T:
    print(t[2])
