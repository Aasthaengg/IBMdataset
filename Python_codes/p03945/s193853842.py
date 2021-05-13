s = input()
n = len(s)
ans = -1
pre = ""

for i in s:
    if i != pre:
        ans += 1
    pre = i

print(ans)