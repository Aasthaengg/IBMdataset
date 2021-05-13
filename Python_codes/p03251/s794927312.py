N,M,X,Y = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))

for Z in range(-100,102):
    if X<Z<=Y and max(x)<Z and min(y)>=Z:
        print('No War')
        break
else:
    print('War')