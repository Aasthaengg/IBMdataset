import itertools

N = int(input())

l = list()
lm = list()
for i in range(N):
    x = int(input())
    l.append(x)
    if x % 10 != 0:
        lm.append(x)

lm = sorted(lm)

a = sum(l)
if a % 10 == 0:
    if lm == []:
        print(0)
    else:
        print(a - lm[0])
else:
    print(a)