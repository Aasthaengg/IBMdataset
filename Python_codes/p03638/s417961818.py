h, w = map(int, input().split())
n = int(input())
ns = map(int, input().split())
s = []
rslt = []
for i, num in enumerate(ns):
    s += [str(i+1)] * num
i = 0
j = 0
while i < h:
    if i % 2 == 0:
        rslt.append(s[i * w:(i + 1) * w])
    else:
        rslt.append(s[i * w:(i + 1) * w][::-1])
    i += 1
for i in range(h):
    print(' '.join(rslt[i]))