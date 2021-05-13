import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

s = LS2()
x,y = MI()

A = []  # 'F'
B = []  # 'T'
r = 0
for i in range(len(s)):
    if i == 0:
        if s[i] == 'F':
            A.append(1)
        else:
            r = 1
            B.append(1)
    else:
        if s[i] == s[i-1]:
            if r == 0:
                A[-1] += 1
            else:
                B[-1] += 1
        else:
            if r == 0:
                B.append(1)
            else:
                A.append(1)
            r = 1-r

C = []  # x軸方向
D = []  # y軸方向
if s[0] == 'F':
    x -= A[0]
    del A[0]
r = 0  # 0ならx軸方向、1ならy軸方向
for i in range(len(A)):
    if (r + B[i]) % 2 == 0:
        C.append(A[i])
        r = 0
    else:
        D.append(A[i])
        r = 1

# Cの各々の元を、1倍か-1倍して全て加えた時にxにできるか
# Dの各々の元を、1倍か-1倍して全て加えた時にyにできるか

if (x+sum(C)) % 2 != 0:
    print('No')
    exit()
x = (x+sum(C)) // 2

if (y+sum(D)) % 2 != 0:
    print('No')
    exit()
y = (y+sum(D)) // 2

if x < 0 or y < 0:
    print('No')
    exit()

# Cの元をいくつか選んで和をとることで、xを作れるか
# Dの元をいくつか選んで和をとることで、yを作れるか

C = [0] + C
from itertools import accumulate
E = list(accumulate(C))
e = 0
if x == 0:
    e = 1
for i in range(1,len(C)):
    for j in range(i,len(C)):
        if E[j] - E[i-1] == x:
            e = 1
if e == 0:
    print('No')
    exit()

D = [0] + D
from itertools import accumulate
F = list(accumulate(D))
f = 0
if y == 0:
    f = 1
for i in range(1,len(D)):
    for j in range(i,len(D)):
        if F[j] - F[i-1] == y:
            f = 1
if f == 0:
    print('No')
else:
    print('Yes')
