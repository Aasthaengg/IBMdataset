s = input()
sl = len(s)
div = ['dream', 'dreamer', 'erase', 'eraser']

s = s[::-1]
ans = ""
for i in range(4): div[i] = div[i][::-1]

for i in range(sl):
    ans += s[i]
    if ans in div:
        ans = ""

if len(ans) == 0:
    print("YES")
else:
    print("NO")