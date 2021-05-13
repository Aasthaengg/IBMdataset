import sys
## io ##
def IS(): return sys.stdin.readline().rstrip()
def II(): return int(IS())
def MII(): return list(map(int, IS().split()))
def MIIZ(): return list(map(lambda x: x-1, MII()))
#======================================================#
def main():
    n = II()
    aa = MII()
    bb = MII()
    ra = rb = 0
    for a,b in zip(aa,bb):
        if a>b: ra += a-b
        if b>a: rb += (b-a)//2
    if rb >= ra: print('Yes')
    else: print('No')

if __name__ == '__main__':
    main()