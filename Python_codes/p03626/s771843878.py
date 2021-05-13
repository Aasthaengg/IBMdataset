

def submit():
    n = int(input())
    s1 = input()
    s2 = input()
    modp = 1000000007

    curr = 0
    ans = 1
    prev = 0 # 縦向きなら1, 横向きなら2
    while curr < n:
        if s1[curr] == s2[curr]:
            # 縦向き
            if prev == 0:
                ans = 3
            elif prev == 1:
                ans *= 2
                ans %= modp
            prev = 1
            curr += 1
        else:
            if prev == 0:
                ans = 6
            elif prev == 1:
                ans *= 2
                ans %= modp
            else:
                ans *= 3
                ans %= modp
            prev = 2
            curr += 2
    print(ans)


submit()