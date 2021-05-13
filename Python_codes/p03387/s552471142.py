# coding:utf-8
a, b, c = map(int, input().split())
m = max(a, b, c)
s = a + b + c
diff = 3 * m - s

if diff % 2 == 0:
    ans = diff // 2
else:
    ans = (diff // 2) + 2

print(ans)
