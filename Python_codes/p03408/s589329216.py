dic = {}
n = int(input())
for i in range(n):
    s = str(input())
    dic.setdefault(s,0)
    dic[s] += 1
m = int(input())
for j in range(m):
    t = str(input())
    dic.setdefault(t,0)
    dic[t] -= 1
ans = max(dic.values())
if ans<0:
    ans = 0
print(ans)