sa = input()
sb = input()
sc = input()

next = "a"
while True:
    if next == "a":
        if sa == "": break
        next = sa[0]
        sa = sa[1:]
    elif next == "b":
        if sb == "": break
        next = sb[0]
        sb = sb[1:]
    else:
        if sc == "": break
        next = sc[0]
        sc = sc[1:]
if next == "a":
    print("A")
elif next == "b":
    print("B")
else:
    print("C")