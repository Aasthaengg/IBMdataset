N = int(input())
def q(i):
    print(i)
    r = input()
    if r[0]=='V': exit()
    return (r[0]=='M') ^ i%2

X = q(0)
def is_ok(m):
    if m==N: return False
    return q(m)==X
ok = 0
ng = N
while ng-ok > 1:
    m = (ok+ng)//2
    if is_ok(m):
        ok = m
    else:
        ng = m