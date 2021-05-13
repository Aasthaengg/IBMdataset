N, M, X, Y = map(int, input().split())
 
x = list(map(int, input().split()))
y = list(map(int, input().split()))
 
for z in range(X, Y+1):
    if X < z <= Y and max(x) < z and min(y) >= z:
        print('No War')
        break
else:
    print('War')