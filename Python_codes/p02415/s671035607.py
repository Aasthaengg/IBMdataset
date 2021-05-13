line = input()
result = []
for c in line:
    num = ord(c)
    if num >= ord("A") and num <= ord("Z"):
        c1 = chr(ord("a") + num - ord("A"))
        result.append(c1)
    elif num >= ord("a") and num <= ord("z"):
        c1 = chr(ord("A") + num - ord("a"))
        result.append(c1)
    else:
        result.append(c)
print("".join(result))