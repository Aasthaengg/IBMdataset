N, = map(int, input().split())
import sys;input=sys.stdin.readline
X = []
Y = []
for _ in range(N):
    s = input().strip()
    a, b = 0, 0
    for c in s:
        if c == "(":
            a += 1
        else:
            if a > 0:
                a -= 1
            else:
                b += 1
    if a >= b:
        X.append((a, b))
    else:
        Y.append((b, a))
X.sort(key=lambda x:x[1])
Y.sort(key=lambda x:x[1])

s = 0
for i in range(len(X)):
    a, b = X[i]
    if s >= b:
        s += a-b
    else:
        print("No")
        sys.exit()
s2 = 0
for i in range(len(Y)):
    a, b = Y[i]
    if s2 >= b:
        s2 += a-b
    else:
        print("No")
        sys.exit()
if s == s2:
    print("Yes")
else:
    print("No")
