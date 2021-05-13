n = int(input())
s = [input() for i in range(n)]
ruiseki = [[None] * (len(s[i]) + 1) for i in range(n)]

for i in range(n):
    ruiseki[i][0] = 0
    for j, char in enumerate(s[i]):
        if char == "(":
            ruiseki[i][j + 1] = ruiseki[i][j] + 1
        else:
            ruiseki[i][j + 1] = ruiseki[i][j] - 1


first = []
second = []
now_m = 0
now_s = 0
for i in range(n):
    min_, sum_ = min(ruiseki[i]), ruiseki[i][-1]
    if sum_ > 0:
        first.append((min_, sum_))
    else:
        second.append((min_, sum_))

now_m = 0
now_s = 0

first = sorted(first, reverse=True)
for mi, su in first:
    if now_s + mi < 0:
        print("No")
        exit()
    now_s += su

second = sorted(second, key=lambda x: x[0] - x[1])
for mi, su in second:
    if now_s + mi < 0:
        print("No")
        exit()
    now_s += su

if now_s == 0:
    print("Yes")
else:
    print("No")