N = int(input())
ans = 0
a = 0
b = 0
ba = 0
for _ in range(N):
    S = input()
    ans += S.count('AB')
    if S[0] == 'B' and S[-1] == 'A':
        ba += 1
    if S[0] != 'B' and S[-1] == 'A':
        a += 1
    if S[0] == 'B' and S[-1] != 'A':
        b += 1

if ba == 0:
    print(ans + min(a, b))
else:
    if a + b == 0:
        print(ans + ba - 1)
    else:
        print(ans + ba + min(a, b))
