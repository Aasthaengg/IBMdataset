x = int(input())

flag = False
for ia in range(0, int(x/4) + 1):
    for ib in range(0, int(x/7) + 1):
        if 4 * ia + 7 * ib == x:
            flag = True
            break
    if flag:
        break

if flag:
    print("Yes")
else:
    print("No")