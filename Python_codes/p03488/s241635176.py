S = input()
x, y = map(int, input().split())
M = S.count("F")
F = list(map(len, S.split("T")))
F1 = F[::2]
B1 = 1 << sum(F1)
X = B1
X = X << x if x > 0 else X >> -x
B1 = B1 << F1[0]
for f in F1[1:]:
    B1 = (B1 << f) | (B1 >> f)
b1 = B1 & X
F2 = F[1::2]
B2 = 1 << sum(F2)
Y = B2
Y = Y << y if y > 0 else Y >> -y
for f in F2:
    B2 = (B2 << f) | (B2 >> f)
b2 = B2 & Y
print("YNeos"[not(b1 and b2)::2])