import copy
S = [c for c in input()]

X = [[]]
for i in range(len(S) - 1):
    X0, X1 = [], []
    for x in X:
        x0 = copy.deepcopy(x)
        x0.append(0)
        X0.append(x0)
        x1 = copy.deepcopy(x)
        x1.append(1)
        X1.append(x1)
    X = X0 + X1
Y = []
for x in X:
    bf = ''
    for i in range(len(S)):
        bf = bf + str(S[i])
        if i == len(S) - 1 or x[i] == 1:
            Y.append(int(bf))
            bf = ''
    if bf != '':
        Y.append(int(bf))
print(sum(Y))
