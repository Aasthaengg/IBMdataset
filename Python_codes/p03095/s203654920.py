import collections

N = int(input())
S = list(input())

MOD = 10 ** 9 + 7
c = collections.Counter(S)
ans = 1
for k, v in c.items():
    ans *= v + 1
    ans %= MOD

ans -= 1
print(ans)
