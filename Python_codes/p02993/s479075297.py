pwd = input()
before = ""
for s in pwd:
    if before == s:
        print("Bad")
        break
    before = s
else:
    print("Good")