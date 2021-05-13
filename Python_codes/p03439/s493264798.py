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

def foo(i):
    print(i,flush=True)
    s = ins()
    a[i] = h[s]
    if h[s]==1:
        exit()

h = {'Vacant':1, 'Male':2, 'Female':3}
n = inn()
a = [0]*(n+1)
foo(0)
a[n] = a[0]
p = 0
q = n
cnt = 1
while q>p+1:
    r = (p+q)//2
    foo(r)
    cnt += 1
    if cnt >= 20:
        exit()
    if a[r]==a[p] and (r-p)%2==1 or a[r]!=a[p] and (r-p)%2==0:
        q = r
    else:
        p = r
        #ddprint(a)
    #ddprint(f"p {p} q {q}")
print("err")
