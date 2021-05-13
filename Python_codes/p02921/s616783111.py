from sys import stdin

S = stdin.readline().rstrip()
T = stdin.readline().rstrip()

ans = 0
for s, t in zip(S, T):
    if (s == t):
        ans += 1

print(ans)