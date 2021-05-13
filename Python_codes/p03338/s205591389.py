# coding:utf-8
n = int(input())
s = input()
ans = 0

for i in range(n):
    right = s[:i]
    left = s[i:]
    tmp = len(set(right) & set(left))
    ans = max(tmp, ans)

print(ans)
