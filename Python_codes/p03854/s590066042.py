s = input()
s = s[::-1]
while s != "":
    if s[:5] == "esare" or s[:5] == "maerd":
        s = s[5:]
    elif s[:6] == "resare":
        s = s[6:]
    elif s[:7] == "remaerd":
        s = s[7:]
    else:
        print("NO")
        exit()
print("YES")