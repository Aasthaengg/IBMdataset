from collections import defaultdict, Counter
n = int(input())
v = [int(x) for x in input().split()]

cnt_even = Counter(v[0::2])
cnt_odd = Counter(v[1::2])

# [(要素, 出現回数), (要素, 出現回数), ....]
common_even = cnt_even.most_common()
common_odd = cnt_odd.most_common()
if len(common_even) == 1:   # 1種類の数しかない
    common_even.append((0, 0))
if len(common_odd) == 1:
    common_odd.append((0, 0))

# 偶数番目に一番多く現れる数と奇数番目に一番多く現れる数が異なる
if common_even[0][0] != common_odd[0][0]:
    ans = n - common_even[0][1] - common_odd[0][1]
else:
    ans = min(n - common_even[1][1] - common_odd[0][1], \
              n - common_even[0][1] - common_odd[1][1])

print(ans)