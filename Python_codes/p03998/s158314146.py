S = [list(input()) for _ in range(3)]
l = 'abc'
num = 0
for i in range(10000):
    if S[num]:
        num = l.find(S[num].pop(0))
    else:
        print(l[num].upper())
        exit()