#Z-Algorithm
#文字列が与えられた時、各 i について「S と S[i:] の最長共通接頭辞の長さ」を記録した配列 A を O(len(S)) で構築するアルゴリズム
#s : 文字列
#あとで要復習！
def z_algorithm(s):
    N = len(s)
    z_alg = [0]*N
    z_alg[0] = N
    i = 1
    j = 0
    
    while i < N:
        while i+j < N and s[j] == s[i+j]: # 伸ばせるだけ伸ばす
            j += 1
        z_alg[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i+k < N and k+z_alg[k] < j: # 今までで求められている場所ならば計算を省略
            z_alg[i+k] = z_alg[k]
            k += 1
        i += k
        j -= k
    return z_alg

n = int(input())
S = input()
max_ = 0
for i in range(n):
    k = S[i:len(S)]
    li = z_algorithm(k)
    for j in range(len(li)):
        if li[j] < j+1:
            max_ = max(max_, li[j])
print(max_)