a = input()

b = a[::-1]

i = 0
while i  < len(b):
    if b[i:i+5] == "esare":
        i += 5
    elif b[i:i+5] == "maerd":
        i += 5
    elif b[i:i+6] == "resare":
        i += 6
    elif b[i:i+7] == "remaerd":
        i += 7
    else:
        ans = "NO"
        break

if i  == len(b):
    ans = "YES"
else:
    ans = "NO"

print(ans)