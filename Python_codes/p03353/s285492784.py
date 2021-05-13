def abc097_c():
    S = str(input())
    K = int(input())
    subs = set()

    for i in range(len(S)):
        for j in range(i+1, min(len(S)+1, i+K+1)):
            subs.add(S[i:j])

    subs_asc = sorted(list(subs))
    ans = subs_asc[K-1]
    print(ans)

abc097_c()