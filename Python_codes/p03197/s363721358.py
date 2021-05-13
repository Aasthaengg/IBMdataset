import sys
## io ##
def IS(): return sys.stdin.readline().rstrip()
def II(): return int(IS())
def MII(): return list(map(int, IS().split()))
def MIIZ(): return list(map(lambda x: x-1, MII()))
#======================================================#
def main():
    n = II()
    aa = [II() for _ in range(n)]
    for a in aa:
        if a%2==1:
            print('first')
            return None
    print('second')
if __name__ == '__main__':
    main()