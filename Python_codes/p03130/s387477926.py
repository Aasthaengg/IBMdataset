s=[list(map(int,input().split())) for i in range(3)]
res = [0]*4
for i in range(len(s)):
    res[s[i][0]-1] += 1
    res[s[i][1]-1] += 1

if max(res) > 2:
    print('NO')
else:
    print('YES')