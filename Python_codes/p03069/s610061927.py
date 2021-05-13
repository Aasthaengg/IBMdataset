n = int(input())
s = str(input())
ans = s.count('.')
L = [[0, s.count('.')]]
for i in range(n):
    if s[i] == '#':
        L.append([L[i][0]+1, L[i][1]])
    else:
        L.append([L[i][0], L[i][1]-1])
    ans = min(ans, L[-1][0] + L[-1][1])
print(ans)
