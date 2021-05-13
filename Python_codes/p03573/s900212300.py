import sys
## io ##
def IS(): return sys.stdin.readline().rstrip()
def II(): return int(IS())
def MII(): return list(map(int, IS().split()))
def MIIZ(): return list(map(lambda x: x-1, MII()))

def main():
    a,b,c = MII()
    if a==b:
        print(c)
    elif a==c:
        print(b)
    else:
        print(a)

if __name__ == '__main__':
    main()