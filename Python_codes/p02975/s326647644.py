from collections import Counter
import sys

n = int(input())
arr = list(map(int, input().split()))

# 全て0ならYes
if all([x == 0 for x in arr]):
    print("Yes")
    sys.exit()

# 3つずつ循環していなければNo
if n % 3 != 0:
    print("No")
    sys.exit()

c = Counter(arr)

# 2種類の場合
if len(c) == 2:
    if c[0] == n // 3:
        print("Yes")
        sys.exit()
    else:
        print("No")
        sys.exit()

# 3種類の場合
elif len(c) == 3:
    result = list(c.values())
    if result[0] == result[1] == result[2]:
        ans1 = True
    else:
        ans1 = False
else:
    print("No")
    sys.exit()

result = list(c.keys())
ans2 = result[0] == result[1] ^ result[2] and result[1] == result[0] ^ result[2] and result[2] == result[0] ^ result[1]

print("Yes" if ans1 and ans2 else "No")