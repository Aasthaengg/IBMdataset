printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True  and False
BIG = 10**18
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

s = ins()
t = ins()
oa = ord('a')
ls = len(s)
nxt = [[-1]*26 for i in range(ls)]
nx = [-1]*26
for i in range(2*ls-1,-1,-1):
    c = ord(s[i%ls])-oa
    for j in range(26):
        if i<ls and nx[j]>=0:
            nxt[i][j] = nx[j]-i
    nx[c] = i
if DBG:
    for i in range(ls):
        #printn(f"{i} ")
        print(nxt[i])

prevpos = nxt[ls-1][ord(t[0])-oa]-1
if prevpos<0:
    print(-1)
    exit()
for i in range(1,len(t)):
    c = ord(t[i])-oa
    nx = nxt[prevpos%ls][c]
    if nx<0:
        print(-1)
        exit()
    prevpos += nx
    #ddprint(f"i {i} pp {prevpos} c {c} ti {t[i]}")
print(prevpos+1)
