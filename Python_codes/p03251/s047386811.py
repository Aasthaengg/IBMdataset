N, M, X, Y = map(int, input().split())

x_list = list(map(int, input().split()))
y_list = list(map(int, input().split()))

x_max = max(x_list)
y_min = min(y_list)

for Z in range(X+1,Y+1):
    if x_max < Z <= y_min:
        print('No War')
        break

else:
    print('War')
