w = list(input())
sw = set(w)
flag = True
for i in sw:
    if w.count(i)%2 != 0:
        flag = False
        break
if flag:
    print("Yes")
else:
    print("No")