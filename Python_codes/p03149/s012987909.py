N = input().split()
flag = True
for i in "1974":
    if not i in N:
        flag = False
print("YES") if flag else print("NO")