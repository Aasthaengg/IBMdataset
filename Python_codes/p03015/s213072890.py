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

l = ins()
a = l[::-1]
n = len(l)
x = 3 if a[0]=='1' else 1
for i in range(1,n):
    if a[i]=='1':
        x = (2*x+pow(3,i,R))%R
print(x)
