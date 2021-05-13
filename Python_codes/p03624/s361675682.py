S = input()
alpha = []

for i in range(97,123):
    alpha.append(chr(i))
    
ans = []
for j in alpha:
    if not j in S:
        ans.append(j)
ans.append(None)

print(ans[0])