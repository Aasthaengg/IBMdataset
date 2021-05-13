n = int(input())
s = input()
e = [0]
w = [0]
for i in range(len(s)):
    if s[i] == 'E':
        e.append(e[i]+1)
        w.append(w[i]+0)
    if s[i] == 'W':
        e.append(e[i]+0)
        w.append(w[i]+1)

ans = float('INF')
for i in range(n):
    iya = (w[i])+(e[n] - e[i+1])
    ans = min(ans,iya)
print(ans)