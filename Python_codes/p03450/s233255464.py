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
def fix(x):
    q = []
    while root[x]!=x:
        q.append(x)
        x = root[x]
    rt = x
    while  len(q)>0:
        x = q.pop()
        dist[x] += dist[root[x]]
        root[x] = rt
    return rt

n,m = inm()
root = list(range(n))
dist = [0]*n
for i in range(m):
    l,r,d = inm()
    l -= 1
    r -= 1
    rtl = fix(l)
    rtr = fix(r)
    if rtl != rtr:
        #ddprint(f'rtl {rtl} rtr {rtr} dl {dist[l]} dr {dist[r]}')
        if dist[l]+d > dist[r]:
            dist[rtr] = dist[l]+d-dist[r]
            dist[r] = dist[l]+d
            root[r] = root[rtr] = rtl
        else:
            dist[rtl] = dist[r]-dist[l]-d
            #dist[l] += dist[rtl]
            dist[l] = dist[r]-d
            root[l] = root[rtl] = rtr
    else:
        if dist[l]+d != dist[r]:
            print('No')
            exit()
    #ddprint(f'l {l} r {r} d {d}')
    #ddprint(root)
    #ddprint(dist)
print('Yes')
