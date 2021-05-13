from collections import Counter
S = input()
ans = []
for i in range(4):
    ans.append(S[i])
ans = Counter(ans)
if len(ans) == 2 and ans[S[0]] == 2:
    print("Yes")
else:
    print("No")
