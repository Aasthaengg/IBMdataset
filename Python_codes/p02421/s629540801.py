s = [0, 0, 0]
loop = int(raw_input())
for i in range(loop):
    w1, w2 = raw_input().split()
    tmp = 1 - cmp(w1, w2)
    if tmp == 1:
        s[0] += 1
        s[2] += 1
    else:
        s[tmp] += 3
print s[0], s[2]
