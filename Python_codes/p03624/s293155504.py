s = input()
alpha = "abcdefghijklmnopqrstuvwxyz"
for a in alpha:
    if a not in s:
        print(a)
        break
else:
    print("None")
