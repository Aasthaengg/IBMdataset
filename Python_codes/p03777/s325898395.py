import sys
## io ##
def IS(): return sys.stdin.readline().rstrip()
def II(): return int(IS())
def MII(): return list(map(int, IS().split()))
def MIIZ(): return list(map(lambda x: x-1, MII()))
#======================================================#
def main():
    a,b = IS().split()
    if a == 'H':
        print(b)
    elif a == 'D':
        if b == 'H':
            print('D')
        elif b == 'D':
            print('H')



if __name__ == '__main__':
    main()