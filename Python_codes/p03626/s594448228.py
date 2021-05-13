import sys


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n = int(input().rstrip('\n'))
    s1 = str(input().rstrip('\n'))
    s2 = str(input().rstrip('\n'))
    cur = 0
    cnt = 1
    f = True
    lv = True
    while cur < n:
        if s1[cur] == s2[cur]:
            #縦の場合
            if f:
                cnt = (cnt * 3) % mod
                f = False
            else:
                if lv:
                    cnt = (cnt * 2) % mod
                else:
                    cnt = (cnt * 1) % mod
            cur += 1
            lv = True
        elif s1[cur] == s1[cur+1] and s2[cur] == s2[cur+1]:
            #横の場合
            if f:
                cnt = (cnt * 6) % mod
                f = False
            else:
                if lv:
                    cnt = (cnt * 2) % mod
                else:
                    cnt = (cnt * 3) % mod
            cur += 2
            lv = False
    print(cnt)


if __name__ == '__main__':
    solve()
