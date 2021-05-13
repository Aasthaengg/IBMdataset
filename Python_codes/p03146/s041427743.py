s = int(input())
li = []
li.append(s)
an = 2
while True:
    if s % 2 == 0:
        s /= 2
    else:
        s = 3*s + 1
    if s in li:
        print(an)
        break
    an += 1
    li.append(s)