N = int(input())
A = [int(i) for i in input().split()]
ls = []
for i, x in enumerate(A):
    ls.append([i+1, x])
ls.sort(key=lambda x: x[1])
cur = 1
num = 0
ans = 0
s = set()
for x, y in ls:
    if cur == y and y not in s and num < x:
        cur += 1
        num = x
        s.add(y)
    else:
        ans += 1
if ans == N:
    print(-1)
else:
    print(ans)