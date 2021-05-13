import sys
input = sys.stdin.readline

S = input().strip()
K = int(input())

count_l = 0
count_r = 0
f = S.count(S[0]) == len(S)
for x in S:
    if x == S[0]:
        count_l += 1
    else:
        break

for x in S[::-1]:
    if x == S[-1]:
        count_r += 1
    else:
        break

ans = 0
for i in range(len(S) - 1):
    if S[i] == S[i + 1]:
        s = S[i]
        ans += 1
        S = S.replace(s * 2, s + '_', 1)

if count_l % 2 and count_r % 2 and S[0] == S[-1]:
    if f:
        ans = ans * K + K // 2
    else:
        ans = (ans + 1) * K - 1
else:
    ans *= K

print(ans)
