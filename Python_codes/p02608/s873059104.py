import sys,collections; input = lambda : sys.stdin.readline()
exec("try:sys.stdin=pen('input.txt','r')\nexcept:pass")
n = int(input())
ans = [0]*100005
for i in range(1,105):
    for j in range(1,105):
        for k in range(1,105):
            v = i**2+j**2+k**2+i*j+j*k+k*i
            if v < 100005:
                ans[v] += 1
for i in range(n):
    print(ans[i+1])
