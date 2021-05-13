import sys
## io ##
def IS(): return sys.stdin.readline().rstrip()
def II(): return int(IS())
def MII(): return list(map(int, IS().split()))
#======================================================#

def main():
    s = IS()
    print(s[0::2])

if __name__ == '__main__':
    main()