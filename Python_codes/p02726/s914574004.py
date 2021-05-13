def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())
import sys
sys.setrecursionlimit(10**6)

n,x,y=sep()



d = [0] * n

for i in range(0, n - 1):
    for j in range(i, n):
        d1 = j - i
        d2 = abs((x - 1) - i) + 1 + abs((y - 1) - j)
        # print(i,j,d1,d2)
        d_min = min(d1, d2)
        d[d_min] += 1
for k in range(1, n):
    print(d[k])




