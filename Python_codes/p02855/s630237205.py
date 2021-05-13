import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))

h,w,k = readints()
s = [readstr() for i in range(h)]

ans = [[0]*w for i in range(h)]

n = 1
for i in range(h):
    a = s[i].count("#")
    if a == 0:
        if i!=0:
            for j in range(w):
                ans[i][j] = ans[i-1][j]
    else:
        f = 0
        for j in range(w):
            if s[i][j] =="#":
                if f:
                    n += 1
                else:
                    f += 1
            ans[i][j] = n
        n += 1

for i in range(h-2,-1,-1):
    for j in range(w):
        if ans[i][j]==0:
            ans[i][j] = ans[i+1][j]

for i in range(h):
    printline(ans[i])





