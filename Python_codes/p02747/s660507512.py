s = input()

for i in range(len(s)):
    if i % 2 == 0:
        if s[i] != "h":
            print("No")
            exit()
    else:
        if s[i] != "i":
            print("No")
            exit()
    if i == len(s) - 1:
        if i % 2 == 1:
            print("Yes")
        else:
            print("No")