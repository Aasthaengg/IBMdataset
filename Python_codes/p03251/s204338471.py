import sys
N,M,X,Y = map(int,input().split())
x =  list(map(int,input().split()))
y =  list(map(int,input().split()))

for Z in range(X+1,Y+1):
    if max(x) < Z and Z <= min(y):
        print("No War")
        sys.exit()
print('War')