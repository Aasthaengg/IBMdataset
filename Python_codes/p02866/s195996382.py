# ？？？？？？？？？？？？？？？？？？？？？？？？？？
# ケース12と13、完全にバグとしか思えないのですが?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????

# もしかして：頂点1は必ず0？

n = int(input())
a = list(map(int, input().split()))
if a[0] != 0:
    print(0)
    exit()
a = sorted(a)
d = {}
for av in a:
    if av not in d:
        d[av] = 1
    else:
        d[av] += 1

if d[0] != 1:
    print(0)
    exit()
MOD = 998244353

ans = 1
for i in range(1, a[-1] + 1):
    if i not in d:
        ans = 0
        break
    ans *= pow(d[i - 1], d[i], MOD)
print(ans % MOD)