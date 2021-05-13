from sys import stdin
S = stdin.readline().rstrip()
len_S = len(S)
if len_S % 2 == 0:
    atcodeer = "gp"*(len_S//2)
else:
    atcodeer = "gp"*(len_S//2)+"g"

ans = 0
for s1, s2 in zip(S, atcodeer):
    if s1 == 'g' and s2 == 'p':
        ans += 1
    elif s2 == 'g' and s1 == 'p':
        ans -= 1
print(ans)