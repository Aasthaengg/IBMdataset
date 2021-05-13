import sys
from collections import Counter

N = int(input())
s = Counter(list(map(int, sys.stdin.readline().rsplit())))

# すべて同じ値かつ0である
if len(s) == 1 and 0 in s:
    print("Yes")
# 2種類の値かつ(a, a, 0)という組み合わせ(aは任意)
elif len(s) == 2 and s[0] == N // 3:
    print("Yes")
# すべて異なる値
elif len(s) == 3:
    res = 0
    num = set()
    # 3種類のXORを計算(res), それぞれの数をpush
    for k, v in s.items():
        res ^= k
        num.add(v)
    # res = a1 ^ a2 ^ a3 = 0 かつそれぞれの数が同じ(= 3 // N) -> Yes
    if not res and len(num) == 1:
        print("Yes")
    else:
        print("No")
# 3種類より多い場合は成立しない
else:
    print("No")
