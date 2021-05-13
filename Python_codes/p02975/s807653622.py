import sys
from collections import Counter
n = int(input())
a = list(map(int, input().split()))


# 全て0ならYes
if all([x == 0 for x in a]):
    print("Yes")
    sys.exit()

    
# 全て0でない場合、nは必ず3の倍数になる
if n % 3 != 0:
    print("No")
    sys.exit()

c = Counter(a)

cli = list(c.keys())
cval = list(c.values())


# 排他的論理和は3つずつ循環するため、keyは3種類、または0を含む場合2種類になる
if len(cli) > 3 or len(cli) <2:
    print("No")
    sys.exit()

# keyが2種類の場合、0が全体の1/3ならOK
if len(cli) == 2 and 0 in cli:
    if c[0] == n // 3:
        print("Yes")
        sys.exit()
    else:
        print("No")
        sys.exit()

# keyが3種類の場合、全ての値が同数、かつ排他的論理和の関係であればOK
if not all([x == cval[0] for x in cval]):
    print("No")
    sys.exit()

ans_0 = cli[1] ^ cli[2] == cli[0]
ans_1 = cli[2] ^ cli[0] == cli[1]
ans_2 = cli[0] ^ cli[1] == cli[2]

print("Yes" if all([ans_0, ans_1, ans_2]) else "No")