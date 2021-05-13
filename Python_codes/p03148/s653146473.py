N,K = map(int,input().split())
TD = [list(map(int,input().split())) for _ in [0]*N]
TD.sort(key=lambda x:(-x[1],x[0]))
use = TD[:K]
var = set()
lock = []
unlock = []
for t,d in use:
    if t in var:
        unlock.append(d)
    else:
        var.add(t)
        lock.append(d)
unlock.sort(reverse=True)
Dscore = sum(lock) + sum(unlock)
v = len(var)
Vscore = v*v
ans = Dscore + Vscore
unused = TD[K:][::-1]
while unlock and unused:
    t,d = unused.pop()
    if t in var: continue
    trash = unlock.pop()
    var.add(t)
    lock.append(d)
    v += 1
    Dscore += d - trash
    Vscore = v*v
    ans = max(ans,Dscore + Vscore)
print(ans)