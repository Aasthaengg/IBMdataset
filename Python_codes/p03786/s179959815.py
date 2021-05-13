#from collections import deque,defaultdict
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
R = 10**9 + 7
#R = 998244353

def ddprint(x):
  if DBG:
    print(x)

n = inn()
a = inl()
a.sort()
acc = [0]*(n+1)
for i in range(1,n):
    acc[i] = acc[i-1]+a[i-1]
#ddprint(a)
#ddprint(acc)
for i in range(n-1,-1,-1):
    if a[i]>2*acc[i]:
        print(n-i)
        exit()
