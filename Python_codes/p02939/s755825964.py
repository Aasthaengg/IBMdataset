s = input()

ans = 0
pre = ""
now = ""

for c in s:
    now += c

    if pre == now:
        continue
    else:
        ans += 1
        pre = now
        now = ""
print(ans)
