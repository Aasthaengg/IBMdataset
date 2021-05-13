N = int(input())
S1 = input()
S2 = input()

MOD = 1000000007


pattern = []
i = 0
while i < N - 1:
    if S1[i] == S1[i + 1]:
        pattern.append('-')
        i += 2
    else:
        pattern.append('|')
        i += 1
else:
    if i == N - 1:
        pattern.append('|')

cnt = 3 if pattern[0] == '|' else 6
for i in range(1, len(pattern)):
    l = pattern[i - 1]
    r = pattern[i]
    if (l, r) == ('|', '|'):
        cnt *= 2
    elif (l, r) == ('|', '-'):
        cnt *= 2
    elif (l, r) == ('-', '|'):
        cnt *= 1
    elif (l, r) == ('-', '-'):
        cnt *= 3
    else:
        raise Exception
    cnt %= MOD

print(cnt)
