s = input()

if len(s) % 2 == 1:
    print("No")
    exit()
while s:
    if s[:2] == "hi":
        s = s[2:]
    else:
        print("No")
        exit()
print("Yes")