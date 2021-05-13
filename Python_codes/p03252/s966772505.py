s = input()
t = input()

d = {}
ans = True
for i, v in enumerate(s):
    if v not in d:
        if t[i] in d.values():
            ans = False
            break
        else:
            d[v] = t[i]
    else:
        if d[v] != t[i]:
            ans = False
            break
if ans:
    print("Yes")
else:
    print("No")