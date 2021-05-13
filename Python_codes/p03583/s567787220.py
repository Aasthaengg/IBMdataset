import sys
## io ##
def IS(): return sys.stdin.readline().rstrip()
def II(): return int(IS())
def MII(): return list(map(int, IS().split()))
#======================================================#
def main():
    N = II()
    MAX=3500
    for h in range(1,MAX+1):
        for n in range(1,MAX+1):
            d = 4*h*n-N*h-N*n
            if d > 0 and (N*h*n)%d==0:
                print('{} {} {}'.format(h, n, (N*h*n)//d))
                return None

if __name__ == '__main__':
    main()