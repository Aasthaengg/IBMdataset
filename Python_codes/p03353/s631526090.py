def abc097_c():
    S = str(input())
    K = int(input())
    subs = set()

    for l in range(1, K+1):
        for i in range(len(S)):
            subs.add(S[i: i+l])
            # スライスのストップ条件はインデックス外でもよい

    subs_asc = sorted(list(subs))
    ans = subs_asc[K-1]
    print(ans)

abc097_c()