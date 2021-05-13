o = input()
e = input()
length = len(o)

ans = ''

for a in range(length):
    ans += o[a]
    if a < len(e):
        ans += e[a]

print(ans)
