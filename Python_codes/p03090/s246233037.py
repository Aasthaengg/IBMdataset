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

n = inn()
if n%2==0:
    print(n*(n-2)//2)
    for i in range(1,n):
        for j in range(i+1,n+1):
            if i+j!=n+1:
                print("{} {}".format(i,j))
if n%2==1:
    print((n-1)*(n-1)//2)
    for i in range(1,n):
        for j in range(i+1,n+1):
            if i+j!=n:
                print("{} {}".format(i,j))
