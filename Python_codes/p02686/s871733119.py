import sys
n = int(input())
si = []
for _ in range(n):
    s = input()
    l = 0
    r = 0
    count = 0
    for i in range(len(s)):
        if s[i] == "(":
            count += 1
        else:
            count = max(0, count-1)
    l = count
    count = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] == ")":
            count += 1
        else:
            count = max(0, count-1)
    r = count
    si.append((l, r))

minus = []
plus = []
while si:
    a, b = si.pop()
    if a <= b:
        plus.append((a, b))
    else:
        minus.append((b, a))

plus.sort()
minus.sort()
countl = 0
for a, b in plus:
    if countl >= a:
        countl += b-a
    else:
        print("No")
        sys.exit()

countr = 0
for a, b in minus:
    if countr >= a:
        countr += b-a
    else:
        print("No")
        sys.exit()


if countr == countl:
    print("Yes")
else:
    print("No")
