s = list(input())

g = []

g.append(0)
g.append(1)
if len(s) > 1:
    if s[0] == s[1]:
        g.append(1)
    else:
        g.append(2)

    for i in range(3,len(s)+1):
        if s[i-1] != s[i-2]:
            g.append(g[i-1]+1)
        else:
            g.append(g[i-3]+2)

print(g[len(s)])