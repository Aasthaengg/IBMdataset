s = input()
#l = s.__len__()
ans = 0
gt = 0
pt = 0

for i in s:
    if i == "g" and gt > pt:
        ans += 1
        pt += 1
    elif i == "g":
        gt += 1
    elif i == "p" and gt > pt:
        pt += 1
    else:
        ans -= 1
        gt += 1
print(ans)
