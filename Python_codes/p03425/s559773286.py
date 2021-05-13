from itertools import combinations

n = int(input())
s = [input() for _ in range(n)]
m = [0]*5
for i in range(n):
    if s[i][0] == 'M':
        m[0] += 1
    elif s[i][0] == 'A':
        m[1] += 1
    elif s[i][0] == 'R':
        m[2] += 1
    elif s[i][0] == 'C':
        m[3] += 1
    elif s[i][0] == 'H':
        m[4] += 1

ans = 0
for i,j,k in combinations(range(5),3):
    ans += m[i]*m[j]*m[k]
print(ans)