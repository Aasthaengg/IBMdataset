s = input()
K = int(input())
n = len(s)

x = dict()
y = []
for i in range(5000):
    y.append([])

#O(N^2)
"""
for i in range(n):
    t = ""
    for j in range(i,n):
        t += s[j]
        if len(t) in x:
            if t not in y[len(t)]:
                y[len(t)].append(t)
        else:
            x[len(t)] = t
            y[len(t)].append(t)
X = []
for i in range(5000):
    if len(y[i]) == 0:
        continue
    y[i].sort()
    for j in range(len(y[i])):
        X.append(y[i][j])
"""
for i in range(n):
    t = ""
    for j in range(i,i+1+K):
        if j > (n-1):
            break
        t += s[j]
        x[t] = t
X = []
for i in x:
    X.append(i)
X.sort()


#print(X)
print(X[K-1])