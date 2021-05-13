X = input()
def solve(X):
    ns = 0
    nt = 0
    for x in X:
        if x == 'S':
            ns += 1
        elif ns>0:
            ns -= 1
        else:
            nt += 1
    return ns+nt
print(solve(X))