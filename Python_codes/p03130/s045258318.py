# coding: utf-8
# Your code here!
x = []
for i in range(3):
    p, q = map(int, input().split())
    x.append(p)
    x.append(q)
ans = []
for i in range(4):
    ans.append(x.count(i + 1))
ans.sort()
if ans == [1, 1, 2, 2]:
    print('YES')
else:
    print('NO')
