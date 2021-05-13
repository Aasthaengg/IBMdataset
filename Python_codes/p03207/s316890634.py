N = int(input())
P = [int(input()) for X in range(0,N)]
P[P.index(max(P))] = max(P)//2
print(sum(P))