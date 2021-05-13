s = input()

g = []
g.append(1)
g.append(2 if s[0] != s[1] else 1)
g.extend([0]*(len(s)-2))

for i in range(2, len(s)):
    g[i] = g[i-1] + 1 if s[i] != s[i-1] else g[i-3] + 2

print(g[-1])
