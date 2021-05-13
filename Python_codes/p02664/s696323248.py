
t = input()
ans = []
for ti in t:
    if ti == "?":
        ans.append("D")
    else:
        ans.append(ti)
print(''.join(ans))