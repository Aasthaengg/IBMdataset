# B - AcCepted

S = list(str(input()))
ans = 'AC'
if S[0] != 'A':
    ans = 'WA'
else:
    S[0] = 'a'

cnt = 0
for i in range(2, len(S)-1):
    if S[i] == 'C':
        cnt += 1
        S[i] = 'c'
if cnt != 1:
    ans = 'WA'

for s in S:
    if s.islower() == False:
        ans = 'WA'
        break

print(ans)
