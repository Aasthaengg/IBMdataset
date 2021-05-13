n = int(input())
a = [int(input()) for i in range(n)]

b = sorted(a)
fst = b[-1]
snd = b[-2]

for x in a:
    if x == fst:
        print(snd)
    else:
        print(fst)


