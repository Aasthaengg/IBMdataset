X = [0] * 5

for c in range(5):
    ABC = input()
    X[c] = [int(ABC), int(ABC[-1])]
    if X[c][1] == 0:
        X[c][1] = 10
        X[c].append(X[c][0])
    else:
        X[c].append(X[c][0] + (10 - X[c][1]))

X.sort(reverse=True, key=lambda val:val[1])

ans = sum([X[x][2] for x in range(4)]) + X[4][0]

print(ans)