N = int(input())

def query(i):
    print(i)
    s = input()[0]
    if s=='V':
        exit()
    return s

a = query(0)

def is_ok(k):
    if k==N: return False
    r = query(k)
    if k%2:
        return r != a
    else:
        return r == a

ok = 0
ng = N
while ng-ok > 1:
    m = (ok+ng)//2
    if is_ok(m):
        ok = m
    else:
        ng = m