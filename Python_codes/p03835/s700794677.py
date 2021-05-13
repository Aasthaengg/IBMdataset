from itertools import combinations
K, S = map(int, input().split())
ans = 0
if K*3 < S:
    print(0)
else:
    for i in range(K+1):
        for j in range(K+1):
            if S-i-j < 0: break
            elif S-i-j <= K: ans += 1
    print(ans)
