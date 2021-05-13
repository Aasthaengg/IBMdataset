T = list(input())+["a"]
for i in range(len(T)):
    s = T[i:i+2]
    if "?" not in s:
        continue
    else:
        if s == ["?","?"]:
            T[i:i+2] = ["P","D"]
        elif s[0] == "?":
            if s[1] == "D":
                T[i] = "P"
            else:
                T[i] = "D"
        if s[1] == "?":
            if s[0] == "P":
                T[i+1] = "D"
            elif i == len(T)-2:
                T[i+1] == "D"
print("".join(T[:-1]))

