S = input()
K = int(input())
Ans = []
for s in S[:-1]:
    if s == 'a':
        Ans.append('a')
        continue
    if (123 - ord(s)) <= K:
        Ans.append('a')
        K -= 123 - ord(s)
    else:
        Ans.append(s)

K %= 26
if ord(S[-1]) + K >= 123:
    Ans.append(chr(ord(S[-1]) + K - 26))
else:
    Ans.append(chr(ord(S[-1]) + K))


print(''.join(Ans))