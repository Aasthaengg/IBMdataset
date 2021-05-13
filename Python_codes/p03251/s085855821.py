N, M, X, Y = map(int, input().split())
X_list = list(map(int, input().split()))
Y_list = list(map(int, input().split()))
X_list.append(X)
Y_list.append(Y)
if max(X_list) < min(Y_list):
    print('No War')
else:
    print('War')

