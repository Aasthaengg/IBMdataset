import itertools

n = int(input())

M = 0
A = 0
R = 0
C = 0
H = 0

for i in range(n):
    s = list(input())
    if s[0] == 'M':
        M += 1
    elif s[0] == 'A':
        A += 1
    elif s[0] == 'R':
        R += 1
    elif s[0] == 'C':
        C += 1
    elif s[0] == 'H':
        H += 1

memo = [M,A,R,C,H]

ans = 0

for v in itertools.combinations(memo, 3):
    tmp = 1
    for vv in v:
        tmp *= vv
    ans += tmp
print(ans)