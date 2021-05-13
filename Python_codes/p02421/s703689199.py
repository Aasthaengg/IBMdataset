def judge(w1, w2):
    la = len(w1)
    lb = len(w2)
    for i in range(min(la,lb)):
        if w1[i] > w2[i]: return 1
        elif w1[i] < w2[i]: return 2
    if la > lb: return 1
    elif la < lb: return 2
    else: return 0

s = [0, 0, 0]
loop = int(raw_input())
for i in range(loop):
    w = raw_input().split()
    tmp = judge(*w)
    if tmp == 0:
        s[1] += 1
        s[2] += 1
    else:
        s[tmp] += 3
print s[1], s[2]