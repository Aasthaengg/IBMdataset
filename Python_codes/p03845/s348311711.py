import copy
n = int(input())
t = list(map(int, input().split()))
m = int(input())
d = []
ans = []
for i in range(m):
    d.append(list(map(int, input().split())))
for i in range(m):
    s = copy.copy(t)
    s[d[i][0] - 1] = d[i][1]
    ans.append(sum(s))
for i in ans:
    print(i)