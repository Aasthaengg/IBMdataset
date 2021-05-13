import math
N , D = ( int(x) for x in input().split() )
X = [ ]
Y = [ ]

for i in range(N):
    x , y = ( int(x) for x in input().split() )
    X.append(x)
    Y.append(y)


ans = 0
for i in range( N ):
    x1 = X[i]
    y1 = Y[i]
    d = math.sqrt( (x1)**2 + (y1)**2 )
    if d <= D:
        ans += 1

print(ans)