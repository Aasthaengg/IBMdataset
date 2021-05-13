n = int(input())
a, b = [0] * n, [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())
a.sort()
b.sort()
if n % 2:
    under = a[n // 2]
    upper = b[n // 2]
    print(upper - under + 1)
else:
    under = a[n // 2 - 1] + a[n // 2]
    upper = b[n // 2 - 1] + b[n // 2]
    print((upper - under) + 1)
"""
# 　どのx　もその中に持てない区間が何個あるかを累積和で持っておく。
aa, ba, aidx = zip(*sorted(zip(a, b, range(n))))  # aでソート
bb, ab, bidx = zip(*sorted(zip(b, a, range(n))))  # aでソート

if n % 2:
    print(bb[n // 2] - aa[n // 2] + 1)
else:
    if aidx[n // 2 - 1] == bidx[n // 2]:
        ans = (bb[n // 2 - 1] - aa[n // 2 - 1] + 1) * (bb[n // 2] - aa[n // 2] + 1)
    else:
        ans = (bb[n // 2 - 1] - aa[n // 2 - 1] + 1) * (bb[n // 2 - 1] - aa[n // 2] + 1)
    print(ans)"""
