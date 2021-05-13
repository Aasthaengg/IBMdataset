#各隣接組の期待値の線形和
n,m,d = map(int, input().split( ))
if d:
    print( (m-1) * 2*( (n-d)/(n*n) ) )
else:
    print(  (m-1) * ( (n-d)/(n*n) ) )