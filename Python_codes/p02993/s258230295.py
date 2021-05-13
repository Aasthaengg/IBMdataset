S = input()

pre = ""
for s in S:
    if pre == s:
        print("Bad")
        exit()
    pre = s

print("Good")
