def dfs(cnt, s, now):
    if cnt == n:
        ans.append(s)
        return
    for i in range(now+1):
        dfs(cnt+1, s+al[i], max(i+1, now))

n = int(input())
ans = []
al = [chr(i) for i in range(97, 97+26)]
dfs(0, "", 0)
for i in ans:
    print(i)