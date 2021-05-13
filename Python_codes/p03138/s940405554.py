from sys import stdout
printn = lambda x: stdout.write(str(x))
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 999999999
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

def h(m):
    sm = 0
    for j in range(m+1):
        sm += max(b[j],n-b[j]) * 2**j
    return sm

def g(k,m):
    if m<0:
        return 0
    if k<2**m:
        return 2**m * b[m] + g(k,m-1)
    return max(2**m * b[m] + h(m-1), \
               2**m * (n-b[m]) + g(k-2**m, m-1))

n,k = inm()
a = inl()
b = [0]*40
for i in range(n):
    for j in range(40):
        b[j] += (a[i]>>j)%2
print(g(k,39))
