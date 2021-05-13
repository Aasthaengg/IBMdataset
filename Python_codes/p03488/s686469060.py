s = list(input())
x, y = map(int, input().split())

s.append("last")
X = []
Y = []
f = "x"
cnt = 0
for i in range(len(s)):
    if s[i] == "F":
        cnt += 1
    elif f == "x":
        X.append(cnt)
        cnt = 0
        f = "y"
    else:
        Y.append(cnt)
        cnt = 0
        f = "x"

if X:
    x -= X[0]
    X.pop(0)

X.sort(reverse=True)
Y.sort(reverse=True)
for i in range(len(X)):
    if x >= 0:
        x -= X[i]
    else:
        x += X[i]
        
for i in range(len(Y)):
    if y >= 0:
        y -= Y[i]
    else:
        y += Y[i]
        
if x == 0 and y == 0:
    print("Yes")
else:
    print("No")