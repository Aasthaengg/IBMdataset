s = list(input())
k = ["k", "e", "y", "e", "n", "c", "e"]
ans = []
i = 0
while s[i] == k[i]:
    ans.append(s[i])
    i += 1
    if i == 7:
        break
for j in range(len(s) - 7 + i, len(s)):
    ans.append(s[j])

jud = True
for j in range(7):
    if ans[j] != k[j]:
        jud = False
if jud:
    print("YES")
else:
    print("NO")