from collections import Counter

S = input()
c = Counter(S)
N = len(S)
ans = 1

for i in range(N-1):
    s = S[i]
    ans += N-c[s]
    c[s] -= 1
    N -= 1

print(ans)