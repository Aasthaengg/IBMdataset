N, M, X, Y = map(int, input().split())
max_X = max(list(map(int, input().split())))
min_Y = min(list(map(int, input().split())))

for Z in range(X+1, Y+1):
    if max_X < Z <= min_Y:
        print("No War")
        exit()
else:
    print("War")
