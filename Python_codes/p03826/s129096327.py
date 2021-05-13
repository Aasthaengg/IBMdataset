x = list(map(int,input().split()))
print( x[0]*x[1] if x[0]*x[1] > x[2]*x[3] else x[2]*x[3])