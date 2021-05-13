# 長さNの文字列Sについて、i=2,3,...,N でのSのi文字目以降から成る文字列とSの最長共通接頭辞の長さ O(N) 
def z_algo(S):
    n = len(S)
    LCP = [0]*n
    i = 1
    j = 0
    c = 0 #最も末尾側までLCPを求めたインデックス
    for i in range(1, n):
        #i番目からのLCPが以前計算したcからのLCPに含まれている場合
        if i+LCP[i-c] < c+LCP[c]:
            LCP[i] = LCP[i-c]
        else:
            j = max(0, c+LCP[c]-i)
            while i+j < n and S[j] == S[i+j]: j+=1
            LCP[i] = j
            c = i
    LCP[0] = n
    return LCP
  
N = int(input())
S = input()

ans = 0
for i in range(N):
  SS = S[i:]
  lcp = z_algo(SS)
  for j in range(len(lcp)):
    l = min(lcp[j], j)
    ans = max(ans, l)

print(ans)