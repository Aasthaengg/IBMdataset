printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True  and False
BIG = 10**18
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

n = inn()
a = inl()
b = [(a[i],i) for i in range(n)]
b.sort(reverse=True)
ddprint(b)
d = [[0]*(n+1) for i in range(n+1)]
for i in range(n):
    v,j = b[i]
    ddprint(f"i {i} v {v} j {j}")
    d[i+1][0] = d[i][0] + v*abs(n-1-i-j) # all to right
    d[i+1][i+1] = d[i][i] + v*abs(j-i) # all to left
    for k in range(1,i+1):
        v1 = d[i][k-1]+v*abs(j-k+1)  # k-1 infants on left
        v2 =  d[i][k]+v*abs(n-1-i+k-j) # i-k infants on right
        ddprint(f"k {k} v1 {v1} v2 {v2} d1 {d[i][k-1]} d0 {d[i][k]} x1 {k-i} x2 {n-1-i+k-j}")
        d[i+1][k] = max(v1,v2)
    if DBG:
        ddprint(i)
        ddprint(d[i+1])
print(max(d[n]))
