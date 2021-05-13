X = input()
l = []
for i in range(len(X)):
    if X[i] == "S":
        l.append("S")
    elif X[i] == "T":
        if len(l) > 0 and l[-1] == "S":
            l.pop(-1)
        #  lが空 or lの末尾がT
        else:
            l.append("T")
ans = len(l)
print(ans)
