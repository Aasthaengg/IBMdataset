import sys
sys.setrecursionlimit(10**8)

N = int(input())
X = str(input())
ones = X.count('1')
intX = int(X, 2)
def check(n, r):
    if n == 0:
        return print(r)
    d = str(bin(n)).count('1')
    check(n%d, r+1)

if ones > 1:
    Xplus = intX % (ones + 1)
    Xminus = intX % (ones - 1)
else:
    Xplus = intX % (ones + 1)
    Xminus = intX

for i in range(N):
    e = 1
    if X[i] == '0':
        num = (Xplus + pow(2, N-1-i, ones + 1)) % (ones + 1)
    elif X[i] == '1' and ones > 1:
        num = (Xminus - pow(2, N-1-i, ones - 1)) % (ones - 1)
    else:
        num = (Xminus - pow(2, N-1-i))
        e = 0
    check(num, e)