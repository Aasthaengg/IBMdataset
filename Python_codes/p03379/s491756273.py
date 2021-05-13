N = int(input())
X = list(map(int, input().split()))

y = sorted(X)

a = y[N//2-1]
b = y[N//2]

for x in X:
    if x <= a:
        print(b)
    else:
        print(a)