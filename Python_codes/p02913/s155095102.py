
# 長さnの文字列Sについて，各iに対しSとS[i:-1]の最長共通接頭辞(LCP)の長さを求める
def Z_algorithm(S): # O(n)
    n = len(S)
    LCP = [0]*n
    i = 1
    j = 0
    LCP[0] = l = n
    while i < l:
        while i+j < l and S[j] == S[i+j]:
            j += 1
        if not j:
            i += 1
            continue
        LCP[i] = j
        k = 1
        while l-i > k < j - LCP[k]:
            LCP[i+k] = LCP[k]
            k += 1
        i += k
        j -= k
    return LCP # LCP:list[int,...] (LCP[i]はSとS[i:-1]の最長共通接頭辞の長さ)



N = int(input())
S = input()
ans = 0
for i in range(N):
    lcp = Z_algorithm(S[i:])
    for j in range(len(lcp)):
        if lcp[j]<=j:
            ans = max(ans,lcp[j])
print(ans)
