from collections import Counter
n = int(input())
a = list(map(int, input().split()))

a = Counter(a)
a = {key: val for key, val in a.items() if val >= 2}
a = dict(sorted(a.items(), reverse=True))

if len(a) == 0:
    print(0)
    exit()

side1 = max(a)
a[side1] -= 2

a = {key: val for key, val in a.items() if val >= 2}
a = dict(sorted(a.items(), reverse=True))

if len(a) == 0:
    print(0)
    exit()

side2 = max(a)

print(side1 * side2)
