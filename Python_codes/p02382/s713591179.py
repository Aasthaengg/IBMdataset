n = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
for i in range(1, 4):
    D = 0
    for j in range(n):
        D += abs(X[j] - Y[j])**(i)
    print(D**(1/i))
print(max(abs(X[i] - Y[i]) for i in range(n)))
