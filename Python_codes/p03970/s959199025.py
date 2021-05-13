from sys import stdin
S = stdin.readline().rstrip()
sign = 'CODEFESTIVAL2016'
ans = 0
for a, b in zip(S, sign):
    if a != b:
        ans += 1
print(ans)