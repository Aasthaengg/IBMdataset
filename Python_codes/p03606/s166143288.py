import sys
## io ##
def IS(): return sys.stdin.readline().rstrip()
def II(): return int(IS())
def MII(): return list(map(int, IS().split()))
def MIIZ(): return list(map(lambda x: x-1, MII()))
#======================================================#
def main():
    n = II()
    cnt = 0
    for _ in range(n):
        l, r = MII()
        cnt += r-l+1
    print(cnt)

if __name__ == '__main__':
    main()