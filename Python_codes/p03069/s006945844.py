N = int(input())
S = input()
n = S.count('.')
ans = min(n, N-n)
lsc = 0
rsc = N-n
for i, c in enumerate(S):
    if c == '#':
        lsc += 1
        rsc -= 1
    a = lsc + ((N-i-1) - rsc)
    ans = min(ans, a)

print(ans)
