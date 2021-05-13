a, b = input().split()
if b == "H":
    b = "HD"
else:
    b = "DH"
print(b[0] if a == "H" else b[1])