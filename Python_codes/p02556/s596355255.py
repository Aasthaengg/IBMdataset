#dt = {} for i in x: dt[i] = dt.get(i,0)+1
import sys;input = sys.stdin.readline
inp,ip = lambda :int(input()),lambda :[int(w) for w in input().split()]

n = inp()
x,y = [],[]
for i in range(n):
    a,b = ip()
    x.append(a+b)
    y.append(a-b)
print(max(max(x)-min(x),max(y)-min(y)))
