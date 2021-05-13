N,A,B = map(int,input().split())
H = [int(input()) for i in range(N)]

def is_ok(k):
    hp = []
    for h in H:
        if h - B*k > 0:
            hp.append(h - B*k)
    if len(hp)==0: return True
    x = 0
    for h in hp:
        x += 0--h//(A-B)
        if x > k: return False
    return True

ok = 10**14
ng = 0
while ok-ng > 1:
    m = (ok+ng)//2
    if is_ok(m):
        ok = m
    else:
        ng = m
print(ok)