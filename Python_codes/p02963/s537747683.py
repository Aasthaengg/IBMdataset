S = int(raw_input())

X1 = 0
Y1 = 0
X2 = 10**9
Y2 = 1

mod = 10**9

if S%mod == 0:
    X3 = 0
    Y3 = S/mod
else:
    Y3 = S/mod + 1
    X3 = mod - S%mod


print X1, Y1, X2, Y2, X3, Y3
