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
    for i in range(n):
        if s[i] == '#':
            cnt_b += 1
        else:
            cnt_w -= 1
        cnt = min(cnt, cnt_b+cnt_w)
    print(cnt)

if __name__ == '__main__':
    main()