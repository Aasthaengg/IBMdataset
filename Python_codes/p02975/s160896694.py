from collections import Counter
n = int(input())
a = list(map(int, input().split()))
s = set(a)
l = len(s)
c = Counter(a)
if l == 1:
    if sum(a) == 0:
        print("Yes")
    else:
        print("No")
elif l == 2:
    x, y = min(a), max(a)
    if x == 0 and c[0] == n / 3:
        print("Yes")
    else:
        print("No")
elif l == 3:
    x, y, z = s
    if x ^ y ^ z == 0 and c[x] == c[y] == c[z]:
        print("Yes")
    else:
        print("No")
else:
    print("No")