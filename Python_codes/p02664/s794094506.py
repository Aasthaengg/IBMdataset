X = input()
ans = []

for i in range(len(X)):
    if X[i] == '?':
        ans.append('D')
    else:
        ans.append(X[i])

for i in ans:
    print(i, end = "")