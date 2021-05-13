N = int(input())
S = [input() for i in range(N)]
ans = dict()
for i in range(N):
    if S[i] in ans:
        ans[S[i]] += 1
    else:
        ans[S[i]] = 1
ans = sorted(ans.items(), key=lambda x:x[1] , reverse = True)
i = 0
kotae = []
while i < len(ans) and ans[0][1] == ans[i][1]:
    kotae.append(ans[i][0])
    i += 1
kotae.sort()
for j in kotae:
    print(j)