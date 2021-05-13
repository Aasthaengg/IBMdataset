S = list(input())
ans = [0] * len(S)

count = 0
for i, s in enumerate(S):
    if S[i] == 'R':
        if S[i+1] == 'L':
            ans[i] += count//2 + 1
            ans[i+1] += count//2 + count%2 + 1
            count = 0
            continue
        count += 1

S.reverse()
ans.reverse()

count = 0
for i, s in enumerate(S):
    if S[i] == 'L':
        if S[i+1] == 'R':
            ans[i] += count//2
            ans[i+1] += count//2 + count%2
            count = 0
            continue
        count += 1

ans.reverse()
print(' '.join(map(str, ans)))