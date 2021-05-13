x = str(input())
ans = len(x)
ns = 0
for i in x:
    if i == "S":
        ns += 1
    elif ns > 0:
        ans -= 2
        ns -= 1

print(ans)
