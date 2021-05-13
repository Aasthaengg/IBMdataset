o = input()
e = input()

ans =""
if len(o) > len(e):
    for i in range(len(e)):
        ans += o[i]
        ans += e[i]
    ans += o[-1]
else:
    for i in range(len(o)):
        ans += o[i]
        ans += e[i]

print(ans)
