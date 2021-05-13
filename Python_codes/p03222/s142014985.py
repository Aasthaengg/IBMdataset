from sys import stdout
printn = lambda x: stdout.write(str(x))
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True  and False
BIG = 999999999
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

def f(n):
    if n<=1:
        return 1
    sm = 2
    for i in range(1,n-1):
        sm += f(n-i-1)
    #ddprint(f"f({n})={sm}")
    return sm

h,w,k = inm()
d = [[0]*(w+2) for i in range(h+1)]
d[0][1] = 1
for i in range(h):
    d[i][0] = d[i][w+1] = 0
    for j in range(1,w+1):
        x = d[i][j]
        #ddprint(f"i {i} j {j} 0inc {x*f(j-1)*f(w-j)}")
        #ddprint(f"i {i} j {j} minc {x*f(j-2)*f(w-j)}")
        #ddprint(f"i {i} j {j} pinc {x*f(j-1)*f(w-j-1)}")
        d[i+1][j] = (d[i+1][j]+x*f(j-1)*f(w-j))%R
        d[i+1][j-1] = (d[i+1][j-1]+x*f(j-2)*f(w-j))%R
        d[i+1][j+1] = (d[i+1][j+1]+x*f(j-1)*f(w-j-1))%R
if DBG:
    for i in range(h+1):
        print(d[i])
print(d[h][k])
