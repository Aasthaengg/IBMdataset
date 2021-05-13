MOD = 1000000007

N = int(input())
S = input()

cnt = {}
for s in S:
    if s not in cnt:
        cnt[s] = 1
    else:
        cnt[s] += 1

ans = 1
for v in cnt.values():
    ans *= v + 1
    ans %= MOD

print(ans - 1)
