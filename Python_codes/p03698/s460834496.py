# B - Varied
S = input()
s = set()
ans = 'yes'
for i in range(len(S)):
    if S[i] in s:
        ans = 'no'
        break
    s.add(S[i])
print(ans)