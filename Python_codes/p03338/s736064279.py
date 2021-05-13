n = int(input())
s = input()
ans = 0
for i in range(n-1):
    s1 = s[:i+1]
    it = iter(s[i+1:])
    it2 = iter(s[i+1:])
    s2 = dict(zip(it,it2))
    visited = {}
    for i in s1:
        if i in visited:
            continue
        if i in s2:
            visited[i] = 1
    ans = max(ans,len(visited))
print(ans)