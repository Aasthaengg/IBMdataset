input()
tmp = 1
for i in map(int, input().split()):
    if tmp <= i:
        tmp = i
    elif tmp <= i + 1:
        tmp = i + 1
    else:
        print("No")
        break
else:
    print("Yes")