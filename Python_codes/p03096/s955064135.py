from collections import defaultdict
 
mod = 10 ** 9 + 7
n = int(input())
C = [int(input()) for i in range(n)]
 
for i in range(n - 1, 0, -1):
    if C[i] == C[i - 1]:
        del C[i]
        #重複部分を圧縮したCを作成
        
D = defaultdict(int)
ans = 1
for c in C:
    ans += D[c]
    D[c] = ans
    #print(D, ans)

print(ans % mod)