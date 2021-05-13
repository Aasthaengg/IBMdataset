n = int(input())

s = [list(map(str, input().split())) for _ in range(n)]
for row in s:
    row[1] = int(row[1])
ss = sorted(s)
ins = 0
ans = list()
tmp = 0
for i in ss:
    if i[0] == tmp:
        ans.insert(ins,i)
    else:
        ins = len(ans)
        ans.append(i)
        tmp = i[0]
for j in ans:
    print(s.index(j)+1)
