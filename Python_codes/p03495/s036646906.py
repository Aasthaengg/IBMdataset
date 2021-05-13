N,K = map(int,input().split())
A = list(map(int,input().split()))
X = dict()
for i in A:
    if i in X:
        X[i] += 1
    else:
        X[i] = 1
Y = [] 
for i in X.keys():
    Y.append(X[i])
Y.sort()
#print(Y)
if len(Y) <= K:
    ans = 0
else:
    ans = sum(Y[:len(Y)-K])
print(ans)