D = int(input())
C = list(map(int, input().split()))
S = [list(map(int, input().split())) for _ in range(D)]

L = [0]*26

v = 0
ans = [0]*D
import copy
for i in range(1, D+1):
    max_ = v
    max_idx = 0
    for j in range(26):
        temp = v
        temp += S[i-1][j]
        L_ = copy.copy(L)
        L_[j] = i
        for k in range(26):
            temp -= C[j]*(i-L_[k])
        if temp >= max_:
            max_ = temp
            max_idx = j
    ans[i-1] = max_idx+1
print(*ans, sep='\n')