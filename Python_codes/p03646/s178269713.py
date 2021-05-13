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
if False and k==0:
    print('2')
    print('0 0')
    exit()
n = 50
p = k//n
r = k%n
if False and p==0:
    print(k+1)
    for i in range(k+1,1,-1):
        printn(str(i)+' ')
    print(0)
    exit()
a = list(range(p+n-1,p-1,-1))
for i in range(r):
    a[i] += 1
print(50)
for i in range(49):
    printn(str(a[i])+' ')
print(a[49])
