n = "keyence"
s = input()

for i in s:
    if n[0] == i:
        n = n[1:]
    else:
        break

for i in s[::-1]:
    if n == "":
        print("YES")
        exit()
    elif n[-1] == i:
        n = n[:-1]
    else:
        break

print("NO")