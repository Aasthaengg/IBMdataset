A,B = map(int,input().split())
X = B % A

if X == 0:
    print(A + B)
else:
    print(B - A)