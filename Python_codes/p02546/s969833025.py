X=list(input())
if X[len(X)-1]=='s':
    X.append('e')
    X.append('s')
else:
    X.append('s')
print("".join(X))