"""
Nが奇数のとき、明らかに掛け算で10の倍数が出来上がらないので、答えは0になる。
Nが偶数のとき、掛け算に巻き込まれる5の素因数の数だけ0ができる。
5^x(1 <= x)ごとに、Nを割る。すると、0~Nに含まれる5^xの数がわかる。
そのうち半分は奇数で半分は偶数である。偶数のカウントだけを加算する。
"""

N = int(input())
if N%2 == 1:
    print(0)
else:
    ans = 0
    x = 1
    while 5**x <= N:
        ans += (N//(5**x))//2
        x += 1
    print(ans)