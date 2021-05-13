n = int(input())
a = list(map(int, input().split()))
"""
４の倍数がn//2個以上
or
全部が２の倍数
"""

n2 = 0
n4 = 0

for _a in a:
    if _a%4 == 0:
        n4 += 1
    elif _a%2 == 0:
        n2 += 1

if n4 + n2//2 >= n//2:
    print("Yes")
else:
    print("No")