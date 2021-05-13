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

h,w,a,b = inm()
for i in range(b):
    print('0'*a+'1'*(w-a))
for i in range(h-b):
    print('1'*a+'0'*(w-a))
