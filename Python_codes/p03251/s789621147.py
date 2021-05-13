N, M, X, Y  = map(int, input().split())
XN = list(map(int, input().split()))
YM = list(map(int, input().split()))

XN.sort()
YM.sort()

print("No War" if max(X,XN[N-1]) < min(Y,YM[0]) else"War")