import collections

n = int(input())
lis = []
for _ in range(n):
    lis.append(int(input()))
    
a = collections.Counter(lis)

ans = 0
for i, j in a.items():
    if j % 2 == 0:
        continue
    else:
        ans += 1
print(ans)