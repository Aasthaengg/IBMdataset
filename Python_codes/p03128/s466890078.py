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

DEPMAX = 5

def foo(n,dep):
    if dep>DEPMAX or n<0:
        ret = "-1"
    elif n==0:
        ret = ""
    elif n%mn==0:
        ret = str(mni)*(n//mn)
    else:
        mxs = "-1"
        for x in a:
            v = foo(n-cs[x],dep+1)
            if v=="-1":
                continue
            vv = v+str(x)
            if int(vv)>int(mxs):
                mxs = vv
            vv = str(x)+v
            if int(vv)>int(mxs):
                mxs = vv
        ret = mxs
    #ddprint(f"foo n {n} k {k} ret {ret}")
    return ret

n,m = inm()
a = inl()
a.sort()
cs = [0,2,5,5,4,5,6,3,7,6]
mn = min([cs[x] for x in a])
for i in range(m-1,-1,-1):
    if cs[a[i]]==mn:
        mni = a[i]
        break
#k = (n+mn-1)//mn
#k = (n)//mn
#ddprint(f"mn {mn} mni {mni}")
#ddprint(a)
print(foo(n,0))
