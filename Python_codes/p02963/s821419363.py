S = int(input())

# if S == (10**18):
#     print(0, 0, 10**9, 0, 1, 10**9)
#     exit()

X1, Y1 = 0, 0

X2 = 10**9
Y3 = -(-S//(10**9))

X3 = 1
Y2 = -(S%-(10**9))

print(X1, Y1, X2, Y2, X3, Y3)