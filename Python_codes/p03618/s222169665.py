import math

ans = 0
S = input()
l = len(S)
ans = l * (l-1) //2 + 1
alpha = {}
for c in S:
    if c not in alpha:
        alpha[c] = 0
    ans -= alpha[c]
    alpha[c] += 1
print(ans)
