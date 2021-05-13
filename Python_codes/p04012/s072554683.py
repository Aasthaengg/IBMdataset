w = input()
d = {}
for i in w:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
ans = "Yes"
for i in d.values():
    if i%2!=0:
        ans = "No"
        break
print(ans)