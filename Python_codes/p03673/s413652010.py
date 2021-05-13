n = int(input())
a = list(map(int, input().split()))
ans = []
for i in a[n-1::-2]:
    ans.append(i)
if n%2:
    res = 1
else:
    res = 0
for i in a[res::2]:
    ans.append(i)
print(*ans)