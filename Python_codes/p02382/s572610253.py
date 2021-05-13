n = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
for p in range(1, 5):
    if p < 4:
        print(sum(abs(x - y) ** p for x, y in zip(X, Y)) ** (1 / p))
    else:
        print(max(abs(x - y) for x, y in zip(X, Y)))