import re

S = input().replace('?', '.')
T = input()

n = len(S)
m = len(T)
j = -1
for i in range(n-m, -1, -1):
    if re.match(S[i:i+m], T):
        j = i
        break

if j == -1:
    print('UNRESTORABLE')
else:
    ans = ''.join(['a' if t == '.' else t for t in S])
    ans = ans[:j] + T + ans[j+m:]
    print(ans)