N = int(input())
S = input()
char = set(list(S))
mod = 10**9+7
ans = 1
for c in char:
    ans *= S.count(c) + 1
    ans %= mod
ans -=1
print(ans)