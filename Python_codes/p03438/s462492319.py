#from collections import deque,defaultdict
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

n = inn()
a = inl()
b = inl()
ia = ib = 0
for i in range(n):
    if a[i]>b[i]:
        ib += a[i]-b[i]
    elif a[i]<b[i]:
        d = b[i]-a[i]
        if d%2==0:
            ia += d//2
        else:
            ia += (d+1)//2
            ib += 1
print('Yes' if ia>=ib else 'No')
