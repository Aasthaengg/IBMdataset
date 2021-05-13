# coding:utf-8
n = int(input())
a = list(map(int, input().split()))
res = a[0::2]
# print(res)
ans = 0

for item in res:
    if item % 2 == 1:
        ans += 1

print(ans)
