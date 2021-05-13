def f():
    s = input()
    for i in range(len(s)):
        if i%2 == 1:
            if s[i] == "L" or s[i] == "U" or s[i] == "D":
                continue
            else:
                return "No"
        else:
            if s[i] == "R" or s[i] == "U" or s[i] == "D":
                continue
            else:
                return "No"
    return "Yes"
print(f())