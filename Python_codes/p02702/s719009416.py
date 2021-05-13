from collections import Counter
MOD = 2019
S = input()
T = [0]
base = 1
for si in reversed(S):
    T += [(T[-1] + int(si) * base) % MOD]
    base = (base * 10) % MOD
ans = 0
for n, count in Counter(T).items():
    ans += count*(count-1)//2
print(ans)
