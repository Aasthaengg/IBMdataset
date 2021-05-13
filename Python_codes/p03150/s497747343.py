T = input()
for f in range(8):
    b = 7-f
    if b and (T[:f] + T[-b:] == "keyence"):
        print("YES")
        exit()
    elif T[-7:] == "keyence":
        print("YES")
        exit()
print("NO")