n,a,b=map(int,input().split())
h=[int(input()) for _ in range(n)]

def hantei(p):
    global a,b
    tp = p
    fa = a - b
    for sh in h:
        sh -= b * p
        if sh > 0:
            tp -= (sh+fa-1) // fa
            if tp < 0:
                return False
    return True


def nibun(l,r):
    if r == l:
        return l
    f = (l+r)//2
    if hantei(f):
        return nibun(l,f)
    else:
        return nibun(f+1,r)

print(nibun(1,10**9))