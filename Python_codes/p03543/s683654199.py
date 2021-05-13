n = input()
for x in range(1, 10):
    if str(x) * 3 in n:
        print("Yes")
        exit()
    elif n[1:] == "000":
        print("Yes")
        exit()
print("No")
