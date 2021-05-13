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
for h in range(1,3501):
    for m in range(1,3501):
        x = 4*h*m-n*m-n*h
        if x>0 and n*h*m%x==0:
            w = n*h*m//x
            print("{} {} {}".format(h,m,w))
            #ddprint(f"{4/n} {1/h+1/m+1/w}")
            exit()
