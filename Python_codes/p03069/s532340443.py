n = int(input())
s = input()
x = 0
y = s.count('.')
c = min(n-y, y)
for i in range(n):
    t = s[i] == '#' #＃であればｔがTrueになる
    x += t
    y -= 1 - t
    c = min(c, x+y)
print(c)