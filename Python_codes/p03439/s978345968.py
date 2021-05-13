N = int(input())
def q(i):
    print(i)
    r = input()[0]
    if r=='V':
        exit()
    return r

z = q(0)
def is_ok(k):
    s = q(k)
    if k%2:
        return z!=s
    else:
        return z==s
ok = 0
ng = N
while ng-ok > 1:
    m = (ok+ng)//2
    if is_ok(m):
        ok = m
    else:
        ng = m
