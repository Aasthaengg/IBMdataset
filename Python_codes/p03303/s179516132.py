s = list(str(input()))
w = int(input())
ans = ''
for i, c in enumerate(s):
    if i%w == 0:
        ans += c
print(ans)
