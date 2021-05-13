import sys
## io ##
def IS(): return sys.stdin.readline().rstrip()
def II(): return int(IS())
def MII(): return list(map(int, IS().split()))
def MIIZ(): return list(map(lambda x: x-1, MII()))
#======================================================#
def main():
    n = IS()
    if '9' in set(n):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()