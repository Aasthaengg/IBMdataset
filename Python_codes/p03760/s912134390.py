o,e = map(list, open(0).read().split())

ans = ''

for i in range(len(o)):
    ans += o[i]
    if i < len(e):
        ans += e[i]

print(ans)