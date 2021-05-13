def main():
    n, m = map(int, input().split())
    P = [0] * m
    S = [0] * m
    for i in range(m):
        P[i], S[i] = map(str , input().split())
    # p = [int(s) for s in p]
    # 問題によってカウントしたい
    WA = [0] * (n+1)
    # 全体として何個かがわかればいい
    AC = [False] * (n+1)
    wa = 0
    for i in range(m):
        p = int(P[i])
        if AC[p]:
            continue
        else:
            if S[i] == 'WA':
                WA[p] += 1
            else:
                AC[p] = True
                wa += WA[p]
    # なぜか都度足さないとWAを間違えている？
    # wa = sum(WA)
    ac = sum(AC)
    print(ac, wa)
        
if __name__ == '__main__':
    main()