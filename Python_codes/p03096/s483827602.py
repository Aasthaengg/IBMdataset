from sys import stdout
printn = lambda x: stdout.write(str(x))
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True  and False
BIG = 999999999
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

n = inn()
c = []
e = [0]*200001
x = [0]*200001
for i in range(n):
    c.append(inn())
ddprint(c)
x[0] = 1
e[c[0]] = 1
for i in range(1,n):
    if c[i]==c[i-1]:
        x[i] = x[i-1]
        continue
    x[i] = (x[i-1]+e[c[i]])%R
    e[c[i]] += x[i-1]
    #ddprint(x[:8])
    #ddprint(e[:8])
print(x[n-1])
