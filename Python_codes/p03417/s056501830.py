n,m = map(int, input().split())

# マス目の上下左右の端が全て表になるので、マス目の総数から引けばOK ※角が重複するので-4をする
if n*m == 1: print(1)
elif n == 1 or m == 1: print(n*m - 2)
else: print(n*m - (2*n+2*m-4))