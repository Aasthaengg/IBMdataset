s = list(input())

if len(s) % 2 == 1:
    print("No")
    exit()

for i in range(len(s)):
    if i % 2 == 0:
        if s[i] == "h":
            continue
        else:
            print("No")
            exit()
    else:
        if s[i] == "i":
            continue
        else:
            print("No")
            exit()
else:
    print("Yes")

