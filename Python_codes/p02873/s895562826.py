s = input()

l = [0]
for c in s:
    if c == "<":
        l.append(l[-1]+1)
    else:
        l.append(0)

r = [0]
for c in s[::-1]:
    if c == ">":
        r.append(r[-1]+1)
    else:
        r.append(0)

ans = 0
for a, b in zip(l, r[::-1]):
    ans += max(a, b)
print(ans)