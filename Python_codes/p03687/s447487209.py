mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    S = input().rstrip('\n')

    ans = 1000
    for i in range(26):
        t = chr(i+97)
        if S == t*len(S):
            print(0)
            exit()
        if t not in S:
            continue
        cnt = 0
        S_tmp = S[:]
        while True:
            ok = 1
            cnt += 1
            new = []
            for j in range(len(S_tmp)-1):
                if S_tmp[j] != t and S_tmp[j+1] != t:
                    ok = 0
                    new.append(S_tmp[j])
                else:
                    new.append(t)
            if ok:
                break
            S_tmp = ''.join(new)
        ans = min(ans, cnt)
    print(ans)


if __name__ == '__main__':
    main()
