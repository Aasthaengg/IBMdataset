import itertools
n = int(input())
sl = []

dic = {'M':0,'A':0,'R':0,'C':0,'H':0}
for i in range(n):
    name = input()
    if name[0] in dic:
        dic[name[0]] += 1

lst = []
for com in itertools.combinations(dic.keys(),3):
    lst.append(com)

ans = 0
for v in lst:
    ans += dic[v[0]] * dic[v[1]] * dic[v[2]]
print(ans)