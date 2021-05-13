import math

S = list(map(int, open(0).read().split()))
N = S[0]
X = S[1:1+N]
Y = S[N+1:]

def calc(p):
    s = 0
    xy = [abs(X[i] - Y[i]) for i in range(N)]
    if p == 1:
        return sum(xy)
    elif p == 2:
        return sum([x ** 2 for x in xy]) ** 0.5
    elif p == 3:
        return sum([x ** 3 for x in xy]) ** (1/3)
    elif p == -1:
        return max(xy)

def show(x):
    print("{:.6f}".format(x))

show(calc(1))
show(calc(2))
show(calc(3))
show(calc(-1))

