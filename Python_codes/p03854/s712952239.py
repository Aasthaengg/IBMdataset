s = str(input())

s = "".join(list(reversed(s)))

y = 0

for _ in range(100000):
    if y == len(s):
        print("YES")
        break
    elif s[y:y+7] == "remaerd":
        y += 7
        #print(y)
    elif s[y:y+6] == "resare":
        y += 6
        #print(y)
    elif s[y:y+5] == "esare":
        y += 5
        #print(y)
    elif s[y:y+5] == "maerd":
        y += 5
    else:
        print("NO")
        break