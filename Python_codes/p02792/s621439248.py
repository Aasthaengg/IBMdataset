from collections import defaultdict

def abc152_d():
    N = int(input())
    freq = defaultdict(int)
    for i in range(1, N+1):
        s = str(i)
        freq[(s[0], s[-1])] += 1  # (先頭,末尾) となる個数を数える

    ans = 0
    for i in range(1, N+1):
        s = str(i)
        ans += freq[(s[-1], s[0])]  # ペアになる (末尾, 先頭) の個数を足していく
    print(ans)

abc152_d()