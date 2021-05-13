# 等差数列 or 例外
import sys
from collections import Counter

s = sys.stdin.readline().rstrip()
k = int(sys.stdin.readline())

ans = 0

def f(s):
    num = 0
    prev = s[0]
    counter = 1
    for letter in s[1:]:
        if prev != letter:
            num += counter // 2
            counter = 1
            prev = letter
        else:
            counter += 1
    num += counter // 2
    return num


if len(Counter(s)) == 1:
    ans = len(s) * k // 2
else:
    s1 = f(s)
    s2 = f(s+s) - s1
    ans = s1 + s2 * (k-1)

print(ans)
