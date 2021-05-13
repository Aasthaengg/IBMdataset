n, m, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
z = min(y)
if z > max(x) and z > X and z <= Y:
    print('No War')
else:
    print('War') 
