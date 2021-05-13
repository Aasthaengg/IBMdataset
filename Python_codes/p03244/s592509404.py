from collections import Counter
n = int(input())
v = list(map(int, input().split()))
v1 = Counter(v[::2])
v2 = Counter(v[1::2])
E = v1.most_common()
O = v2.most_common()
if E[0][0] == O[0][0]:
    tmp1 = E[1][1] if len(E) > 1 else 0
    tmp2 = O[1][1] if len(O) > 1 else 0
    ans = min(n-E[0][1]-tmp2, n-tmp1-O[0][1])
else:
    ans = n-E[0][1]-O[0][1]
print(ans)