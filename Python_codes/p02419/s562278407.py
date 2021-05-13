w = raw_input().upper()
s = 0
while True:
    t = raw_input()
    if t !=  "END_OF_TEXT":
        for i in t.split() :
            if w == i.upper():
                s += 1
    else :
        break

print s