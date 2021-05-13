k, x = map(int, input().split())
a = k * 2 - 1
b = x - k + 1
ans = []
#
for i in range(b,b + a):
    ans.append(i)
map = map(str, ans)
print(' '.join(map))