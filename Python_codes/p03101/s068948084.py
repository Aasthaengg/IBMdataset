X = list(map(int,input().split()))

x = list(map(int,input().split()))

HW = X[0] * X[1]

h = X[1] * x[0]
w = (X[0] * x[1]) - (x[0] * x[1])

print( HW - ( h+w ) )

