n = int(input())
S = input()
re = 0
for s in S:
    if s == 'E':
        re += 1
lw = 0
c = len(S)
for i in range(n):
    if S[i]  == 'E':
        re -= 1
    c = min(c, re+lw)

    if S[i] == 'W':
        lw += 1
print(c)
