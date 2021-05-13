N,R = (input().split())
X = int(N)
Y = int(R)
a = (Y + (100 * (10 - X)) )
if X >= 10:
    print(Y)
else:
    print(a)