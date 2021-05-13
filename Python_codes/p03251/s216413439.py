import sys

N, M, X, Y = map(int, input().split())
X_lis = list(input().split())
X_lis = [int(X_lis[i]) for i in range(N)]
Y_lis = list(input().split())
Y_lis = [int(Y_lis[i]) for i in range(M)]

for Z in range(X+1, Y+1):
    if Z > max(X_lis) and Z <= min(Y_lis):
        print('No War')
        sys.exit()
    
print('War')
