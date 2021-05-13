from sys import stdout
import sys,resource
printn = lambda x: stdout.write(x)
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
DBG = True  and False
BIG = 999999999
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

k = inn()
a = inl()
if k==1:
    if a[0]==2:
        print("2 3")
    else:
        print(-1)
    exit()
l = r = 2
for i in range(k-1,-1,-1):
    mn = ((l+a[i]-1)//a[i])*a[i]
    mx = (r//a[i])*a[i]+a[i]-1
    if mn>mx:
        print(-1)
        exit()
    l = mn
    r = mx
print("{} {}".format(l,r))
