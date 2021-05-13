s = input()
d = {}
flag = 1
for i in s:
    d.setdefault(i, 0)
    d[i] += 1


for j in d.values():
    if j % 2 != 0:
        flag = 0
        break
    
if flag == 0:
    print("No")
else:
    print("Yes")