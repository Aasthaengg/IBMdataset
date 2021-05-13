S = list(input())
N = len(S)

ans = 'AC'
if S[0] != 'A' or 'C' not in S[2:-1]:
    ans = 'WA'

tmp = 0
for i in range(1,N):
    if S[i].isupper():
        tmp += 1

if tmp > 1:
    ans = 'WA'

print(ans)
