import sys
S = list(input())
x, y = map(int, input().split())
c = 0
p = 0
q = 0
now = 0
R = []
L = []
for i in range(len(S)):
    if S[i] == "T":
        if p != 0:
            R.append(p)
            p = 0
        elif q != 0:
            L.append(q)
            q = 0
        c += 1
    elif c == 0:
        now += 1
    elif c % 2 == 0:
        p += 1
    else:
        q += 1
if p != 0:
    R.append(p)
if q != 0:
    L.append(q)

A = 2*(sum(R)+now)
B = 2*(sum(L))
dp_x = [[0]*(A+2) for _ in range(len(R)+2)]
dp_y = [[0]*(B+2) for _ in range(len(L)+1)]
c = 0
dp_x[0][sum(R)+now] = 1
dp_y[0][sum(L)] = 1
for i in range(1, len(R)+2):
    for j in range(A+2):
        if i == 1:
            if j - now >= 0:
                if dp_x[i-1][j-now] == 1:
                    dp_x[i][j] = 1
        else:
            if j - R[i-2] >= 0:
                if dp_x[i-1][j-R[i-2]] == 1:
                    dp_x[i][j] = 1
            if j + R[i-2] <= A+1:
                if dp_x[i-1][j+R[i-2]] == 1:
                    dp_x[i][j] = 1

for i in range(1, len(L)+1):
    for j in range(B+2):
        if j - L[i-1] >= 0:
            if dp_y[i-1][j-L[i-1]] == 1:
                dp_y[i][j] = 1
        if j + L[i-1] <= B+1:
            if dp_y[i-1][j+L[i-1]] == 1:
                dp_y[i][j] = 1

if A + 1 < x+sum(R)+now or x+sum(R)+now < 0:
    print("No")
    sys.exit()

if B + 1 < y+sum(L) or y+sum(L) < 0:
    print("No")
    sys.exit()

if dp_x[len(R)+1][x+sum(R)+now] == 1 and dp_y[len(L)][y+sum(L)] == 1:
    print("Yes")
else:
    print("No")