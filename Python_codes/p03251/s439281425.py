N, M, X, Y = map(int, input().split())

x = list(map(int, input().split()))
y = list(map(int, input().split()))

x_max = max(x)
y_min = min(y)

for z in range(X+1, Y+1):
    if z > x_max and z <= y_min:
        print("No War")
        exit()

print("War")