n, m, x, y = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
for i in range(x + 1, y + 1):
    if max(X) < i and min(Y) >= i:
        print("No War")
        exit()
print("War")