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

def foo(x):
    k = b*x
    sm = 0
    for i in range(n):
        sm += max(0, (h[i]-k+c-1)//c)
    #ddprint(f"foo {x} sm {sm}")
    return (sm<=x)

n,a,b = inm()
h = []
for i in range(n):
    h.append(inn())
c = a-b
mn = 0
mx = (max(h)+b-1)//b
while mx>mn+1:
    mid = (mx+mn)//2
    if foo(mid):
        mx = mid
    else:
        mn = mid
print(mx)
