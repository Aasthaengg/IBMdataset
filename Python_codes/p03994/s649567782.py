s = str(input())
k = int(input())
S = []
for i in range(len(s)):
    S.append(ord(s[i]) - 97)
i = 0
while k > 0:
    if S[i] > 0 and 26 - S[i] <= k:
        k -= 26 - S[i]
        S[i] = 0
        i += 1
    else:
        i += 1
    if i >= len(s):
        S[-1] += k
        break
ans = ''
for x in S:
    ans += chr((x % 26) + 97)
print(ans)
