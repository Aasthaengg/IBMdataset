n = int(input())

X = [0]*(n+1)
for i in range(1, n+1):
    X[i] += 1
    j = 2*i
    while j <= n:
        X[j] += 1
        j += i
#print(X[0:10])

ans = 0
for k in range(1, n+1):
    ans += k*X[k]
print(ans)
