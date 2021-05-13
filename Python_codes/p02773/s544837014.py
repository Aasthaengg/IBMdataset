n = int(input())
a = [input() for _ in range(n)]
cnt = {}
for i in range(n):
    if a[i] not in cnt:
        cnt[a[i]] = 1
    else:
        cnt[a[i]] += 1
mx = max(cnt.values())
ans = []
for i in cnt.keys():
    if cnt[i] == mx:
        ans.append(i)
ans.sort()
for _ in ans:
    print(_)



