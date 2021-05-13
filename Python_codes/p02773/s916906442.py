n = int(input())
dic = {}
for i in range(n):
    s = str(input())
    if s in dic.keys():
        dic[s] += 1
    else:
        dic.setdefault(s,1)
max_v = max(dic.values())
ans = []
for j in dic.items():
    if j[1] == max_v:
        ans.append(j[0])
ans.sort()
for i in ans:
    print(i)
