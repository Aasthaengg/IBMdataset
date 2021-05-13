S = list(input())

ans = []
cnt = 0
for i in range(len(S)):
    if S[i] in ['A', 'C', 'G', 'T']:
        cnt += 1
    else:
        ans.append(cnt)
        cnt = 0
ans.append(cnt)

print(max(ans))
