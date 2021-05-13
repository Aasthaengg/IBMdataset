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

k = inn()
a = inl()
l = r = 2
for i in range(k-1,-1,-1):
    nl = ((l+a[i]-1)//a[i])*a[i]
    nr = (r//a[i])*a[i] + a[i]-1
    #ddprint("l {} r {} nl {} nr {}".format(l,r,nl,nr))
    if r<nl or nr<l:
        print(-1)
        exit()
    l = nl
    r = nr
print("{} {}".format(l,r))
