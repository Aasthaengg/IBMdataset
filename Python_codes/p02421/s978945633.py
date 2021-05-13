n = int(input())
i = 0
p0 = 0
p1 = 0
while i < n:
    s = list(map(str, input().split(' ')))
    if s[0] > s[1]:
        p0 += 3
    elif s[0] < s[1]:
        p1 += 3
    else:
        p0 += 1
        p1 += 1
    i += 1
print(str(p0) + ' ' + str(p1))
