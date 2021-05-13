import sys

s = list(input())
n = len(s)
t = []
ind = [-1]
for i in range(n):
    if s[i] != "x":
        t.append(s[i])
        ind.append(i)
ind.append(n)
# print(t)
ng = 0
lt = len(t)
for i in range(lt):
    if t[i] != t[lt-1-i]:
        ng = 1
        break
if ng == 1:
    print(-1)
    sys.exit()

ind1 = [ind[i+1]-ind[i] for i in range(len(ind)-1)]
ans = 0
for i in range(len(ind1) // 2):
    ans += abs(ind1[i] - ind1[len(ind1) - 1 - i])
print(ans)