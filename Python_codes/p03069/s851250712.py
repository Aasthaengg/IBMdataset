import sys
## io ##
def IS(): return sys.stdin.readline().rstrip()
def II(): return int(IS())
def MII(): return list(map(int, IS().split()))
#======================================================#
def main():
    n = II()
    s = IS()
    cnt_b = 0
    cnt_w = s.count('.')
    cnt = cnt_w
    for si in s:
        if si == '#':
            cnt_b += 1
        else:
            cnt_w -= 1
        c = cnt_b+cnt_w
        if c < cnt:
            cnt = c
    print(cnt)

if __name__ == '__main__':
    main()