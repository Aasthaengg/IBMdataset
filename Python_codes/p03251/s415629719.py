N, M, X, Y = map(int, input().split())
X_list = [int(i) for i in input().split()]
Y_list = [int(i) for i in input().split()]

found = False
for Z in range(X+1, Y+1):
    if max(X_list) < Z and min(Y_list) >= Z:
        found = True
        print("No War")
        break
if not found:
    print("War")