a = map(int,input().split())
b = sorted(a)
if b[0] != 0 and b[1] != 0 and b[2] != 0:
    if b[2] == b[0] + b[1]:
        print("Yes")
    else:
        print("No")
else:
    print("No")