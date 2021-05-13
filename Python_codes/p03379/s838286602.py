import bisect

N = int(input())
X = list(int(x) for x in input().split())
Y = sorted(X)
m1 = Y[N//2-1]
m2 = Y[N//2]

for x in X:
    if bisect.bisect_left(Y, x) > N//2-1:
        print(m1)
    else:
        print(m2)