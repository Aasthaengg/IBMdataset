def f():
    return int(raw_input())
def f2():
    return map(int, raw_input().split())

def f3(n, AA, x):
    tmp = n + AA[0]
    if len(AA) == 1:
        try: x[tmp] = 1
        except: pass
    else:
        f3(n, AA[1:], x)
        try:
            x[tmp] = 1
            f3(tmp, AA[1:],x)
        except:
            pass
    return

n = f()
A = sorted(f2())
q = f()
M = f2()

x = [0 for i in range(max(M)+1)]
f3(0, A, x)

for e in M:
    if x[e] == 1:
        print 'yes'
    else:
        print 'no'