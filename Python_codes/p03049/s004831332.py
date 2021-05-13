N = int(input())
S = [input() for _ in range(N)]

AB_cnt = 0
c1 = 0
c2 = 0
c3 = 0


for s in S:
    AB_cnt += s.count('AB')
    if s[0] == 'B' and s[-1] == 'A':
        c1 += 1
    elif s[0] == 'B':
        c2 += 1
    elif s[-1] == 'A':
        c3 += 1
if c1 == 0:
    print(AB_cnt + min(c2,c3))
elif c2 + c3 > 0:
    print(AB_cnt + c1 + min(c2,c3))
else:
    print(AB_cnt + c1 - 1)