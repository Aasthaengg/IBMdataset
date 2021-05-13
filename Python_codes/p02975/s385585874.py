import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N = I()
a = LI()

# a_i = a_(i+3) に注目

if N % 3 != 0:
    for i in range(N):
        if a[i] != 0:
            print('No')
            break
    else:
        print('Yes')
    exit()

B = list(set(a))
b = len(B)
n = N//3
if b > 3:
    print('No')
elif b == 1:
    for i in range(N):
        if a[i] != 0:
            print('No')
            break
    else:
        print('Yes')
elif b == 2:
    x,y = B
    c = a.count(x)
    if x != 0 and y != 0:
        print('No')
    elif x == 0:
        if c == n:
            print('Yes')
        else:
            print('No')
    else:
        if c == 2*n:
            print('Yes')
        else:
            print('No')
else:
    x,y,z = B
    c = a.count(x)
    d = a.count(y)
    if not (c == d == n):
        print('No')
    else:
        if x ^ y == z:
            print('Yes')
        else:
            print('No')
