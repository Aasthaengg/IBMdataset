from collections import Counter
import sys

h, w = map(int, input().split())
arr = [list(map(str, input().rstrip())) for _ in range(h)]

arr = sum(arr, [])

c = Counter(arr)
c = list(c.values())

if h % 2 == 0 and w % 2 == 0:
    ans = all([x % 4 == 0 for x in c])

elif h % 2 == 1 and w % 2 == 1:
    even = (h + w) // 2 - 1
    odd_cnt = len([x for x in c if x % 2 == 1])
    if odd_cnt != 1:
        print("No")
        sys.exit()
    odd = sum([x for x in c if x % 2 == 1])
    if odd % 4 == 3:
        even -= 1
    c.remove(odd)
    ans = True if sum([x % 4 == 2 for x in c]) <= even else False
    ans &= all([x % 4 == 0 for x in c if x % 4 != 2])

else:
    even = h // 2 if h % 2 == 0 else w // 2
    ans = True if sum([x % 4 == 2 for x in c]) <= even else False
    ans &= all([x % 4 == 0 for x in c if x % 4 != 2])

print("Yes" if ans else "No")