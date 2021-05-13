X, Y = [int(x) for x in input().split()]

def solve(X, Y):
    if X == Y:
        return -1
    if Y < X:
        if X % Y == 0:
            return -1

    for x in range(X, 10**18+1, X):
        if x % Y != 0:
            return x
print(solve(X, Y))



