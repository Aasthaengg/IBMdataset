import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n,g = map(int,readline().split())
XY = []
for i in range(n):
    XY.append(list(map(int,readline().split())))
ans = 10**32

if g == 2:
    for i in range(n):
        for j in range(i+1,n):
            hidarisita = (min(XY[i][0],XY[j][0]),min(XY[i][1],XY[j][1]))
            migiue = (max(XY[i][0],XY[j][0]),max(XY[i][1],XY[j][1]))
            ans = min(ans,abs((migiue[0]-hidarisita[0])*(migiue[1]-hidarisita[1])))

elif g == 3:
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                hidarisita = (min(XY[i][0],XY[j][0],XY[k][0]),
                min(XY[i][1],XY[j][1],XY[k][1]))
                migiue = (max(XY[i][0],XY[j][0],XY[k][0]),
                max(XY[i][1],XY[j][1],XY[k][1]))
                ans = min(ans,abs((migiue[0]-hidarisita[0])*(migiue[1]-hidarisita[1])))
else:

    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    hidarisita = (min(XY[i][0],XY[j][0],XY[k][0],XY[l][0]),
                    min(XY[i][1],XY[j][1],XY[k][1],XY[l][1]))
                    migiue = (max(XY[i][0],XY[j][0],XY[k][0],XY[l][0]),
                    max(XY[i][1],XY[j][1],XY[k][1],XY[l][1]))

                    res = 0
                    for m in range(n):
                        if hidarisita[0] <= XY[m][0] <= migiue[0] and \
                            hidarisita[1] <= XY[m][1] <= migiue[1]:
                            res += 1

                    if res >= g:
                        ans = min(ans,abs((migiue[0]-hidarisita[0])*(migiue[1]-hidarisita[1])))

print(ans)