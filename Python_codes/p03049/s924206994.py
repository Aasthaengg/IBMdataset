def solve():
    n = int(input())
    s = []
    ans = 0
    acnt = 0
    bcnt = 0
    bacnt = 0
    for i in range(n):
        s_i = input()
        ans += s_i.count('AB')
        s_i.replace('AB', '')
        if s_i[0] == 'B' and s_i[-1] == 'A':
            bacnt += 1
        elif s_i[0] == 'B':
            bcnt += 1
        elif s_i[-1] == 'A':
            acnt += 1

    # bacntをa,bに変換
    if bacnt == 0:
        ans += min(acnt, bcnt)
    elif acnt == 0 and bcnt == 0:
        ans += bacnt-1
    else:
        ans += bacnt + min(acnt, bcnt)

    print(ans)

solve()