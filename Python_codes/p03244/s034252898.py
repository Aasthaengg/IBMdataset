from collections import Counter

n = int(input())
V = list(map(int, input().split()))

V_even = V[: : 2]
V_odd = V[1: : 2]

D_even = Counter(V_even)
D_odd = Counter(V_odd)

ans = 0
even, odd = D_even.most_common(2), D_odd.most_common(2)
if even[0][0] != odd[0][0]:
    ans = n - even[0][1] - odd[0][1]
else:
    if len(D_even) == len(D_odd) == 1:
        ans = n // 2
    else:
        ans = min(
            n - even[1][1] - odd[0][1],
            n - even[0][1] - odd[1][1]
        )

print(ans)