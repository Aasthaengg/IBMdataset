S = int(input())
X1, Y1, X2, Y2 = 0, 0, 10**9, 1
shou, amari = divmod(S, 10**9)
 
if amari == 0:
    Y3 = shou
    X3 = 0
else:
    Y3 = shou + 1
    X3 = -(amari - 10**9)
 
print(X1, Y1, X2, Y2, X3, Y3)