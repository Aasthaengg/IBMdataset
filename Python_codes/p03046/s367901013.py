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

m,k = inm()
if m==0 and k==0:
    print('0 0')
    exit()
if m==0 and k>0:
    print('-1')
    exit()
if m==1 and k==0:
    print('0 0 1 1')
    exit()
if m==1 and k>0:
    print('-1')
    exit()
if k>=2**m:
    print('-1')
    exit()

if k==0:
    printn('0 0')
    for i in range(1,2**m):
        printn(' {} {}'.format(i,i))
    print('')
    exit()

u = [False]*(2**m)
u[k] = True
a = []
cnt = 0
for i in range(1,2**m):
    j = i^k
    if not u[i] and not u[j]:
        a.append(i)
        u[j] = True
        cnt += 1
        if cnt==2**(m-1)-1:
            break

s = [x for x in a]
t = [x for x in a]
t.reverse()
s.extend([0,k,0])
s.extend(t)
v = [x^k for x in a]
t = [x for x in v]
t.reverse()
s.extend(v)
s.append(k)
s.extend(t)

printn(s[0])
for i in range(1,len(s)):
    printn(' ' + str(s[i]))
print("")
