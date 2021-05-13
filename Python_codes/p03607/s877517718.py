import collections

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
c = collections.Counter(a)
ans = 0
for k,v in c.items():
    if v % 2 == 0:
        continue
    else:
        ans +=1
print(ans)