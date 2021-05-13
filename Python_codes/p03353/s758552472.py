S = input()
n = len(S)
k = int(input())
cnt = 0
itl = sorted(list(set(S)))
ans = set([])
for w in itl:
    for i, s in enumerate(S):
        if s != w:
            continue
        else:
            for j in range(i+1, i+k+1):
                ans.add(S[i:j])
    cnt += len(ans)
    if cnt >= k:
        break
    else:
        ans.clear()

ans = list(ans)
ans.sort()
index = k - 1 - (cnt - len(ans))
print(ans[index])
