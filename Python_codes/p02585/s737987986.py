import sys

input = sys.stdin.readline
N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))
 
ans = -float('inf')
for s in range(N):
    S = [] 
    i = P[s] - 1
    S.append(C[i])
    while i != s:
        i = P[i] - 1
        S.append(S[-1] + C[i])
 
    if K <= len(S):
        tmp = max(S[:K])
    elif S[-1] <= 0:
        tmp = max(S)
    else:
        # ループの中で最大となるところで止める
        tmp1 = S[-1] * (K // len(S) - 1)
        tmp1 += max(S)
        # 限界まで進む
        tmp2 = S[-1] * (K // len(S))
        r = K % len(S)
        if r != 0:
            tmp2 += max(0, max(S[:r]))
        tmp = max(tmp1, tmp2)
 
    ans = max(ans, tmp)
 
print(ans)