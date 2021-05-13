s = input()[::-1]

while True:
    if len(s) == 0:
        break
    if s[:7] == "remaerd":
        s = s[7:]
    elif s[:6] == "resare":
        s = s[6:]
    elif s[:5] == "maerd" or s[:5] == "esare":
        s = s[5:]
    else:
        print("NO")
        exit()

print("YES")