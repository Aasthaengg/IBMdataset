N = int(input())
X = []
U = []
result = []
for _ in range(N):
    x, u = input().split()
    X.append(float(x))
    U.append(u)
   


for a, b in zip(X, U):
    if b == "BTC":
        result.append(380000 * a)
    else:
        result.append(a)

print(sum(result))
