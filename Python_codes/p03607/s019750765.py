import sys
## io ##
def IS(): return sys.stdin.readline().rstrip()
def II(): return int(IS())
def MII(): return list(map(int, IS().split()))
from functools import partial, reduce
from collections import Counter
#======================================================#
def f_chain(*args):
    return reduce(lambda x, f: f(x), args)
def is_odd(n):
    return n%2==1

def main():
    n = II()
    aa = [II() for _ in range(n)]
    c = Counter(aa)
    f_chain(c.values(),
            partial(filter, is_odd),
            list,
            len,
            print,
    )

if __name__ == '__main__':
    main()