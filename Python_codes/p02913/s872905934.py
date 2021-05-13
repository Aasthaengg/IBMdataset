def Z_algo(S):
    n = len(S)
    LCP = [0] * n
    c = 0  # 最も末尾側までLCPを求めたインデックス
    for i in range(1, n):
        # i番目からのLCPが以前計算したcからのLCPに含まれている場合
        if i + LCP[i - c] < c + LCP[c]:
            LCP[i] = LCP[i - c]
        else:
            j = max(0, c + LCP[c] - i)
            while i + j < n and S[j] == S[i + j]:
                j += 1
            LCP[i] = j
            c = i
    LCP[0] = n
    return LCP


n = int(input())
s = input()
ans = 0
for i in range(n):
    lcp = Z_algo(s[i:])
    for j, p in enumerate(lcp):
        tmp = min(j, p)
        ans = max(ans, tmp)
print(ans)
