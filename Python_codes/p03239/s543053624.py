N, T = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
Y = [x for x in X if x[1]<=T]
Z = [y[0] for y in Y]
print("TLE" if Y==[] else min(Z))