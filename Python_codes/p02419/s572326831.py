W = input()
s = ""
while True:
    a = input()
    try:
        if a == "END_OF_TEXT":
            break
        else:
            s += a.lower()
            s += " "
    except:
        break

t = s.strip(".").split(" ")
print(t.count(W))