N = int(input())
S = input()
x = S.count('E') - (1 if S[0] == 'E' else 0)
ans = x
for s1, s2 in zip(S, S[1:]):
    if s1 == 'W':
        x += 1
    if s2 == 'E':
        x -= 1
    ans = min(ans, x)
print(ans)
