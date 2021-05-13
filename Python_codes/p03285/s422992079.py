N = int(input())
div, mod = divmod(N, 7)
flag = False
for x in range(0, 100, 4):
    for y in range(0, 100, 7):
        if x + y == N:
            flag = True
            break
if flag:
    print("Yes")
else:
    print("No")
