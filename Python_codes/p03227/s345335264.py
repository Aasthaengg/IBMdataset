s = input()
if len(s) == 2:
    print(s)
else:
    for i in range(len(s)-1, -1, -1):
        print(s[i], end="")
