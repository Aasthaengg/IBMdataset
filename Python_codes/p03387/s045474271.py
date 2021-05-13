## C - Same Integers
X = list(map(int, input().split()))
cnt = 0
if sum([x%2 for x in X]) == 2:
    for i in range(3):
        X[i] = X[i] + 1 if X[i]%2 == 1 else X[i]
        cnt = 1
elif sum([x%2 for x in X]) == 1:
    for i in range(3):
        X[i] = X[i] + 1 if X[i]%2 == 0 else X[i]
        cnt = 1
Max = max(X)
X.remove(Max)
print( (2 * Max - sum(X) )//2 + cnt )