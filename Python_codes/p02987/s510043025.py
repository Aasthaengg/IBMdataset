x,y,z,w = input()

l = []
l.append(x)
l.append(y)
l.append(z)
l.append(w)
new_l = sorted(l)

if new_l[0] == new_l[1] and new_l[1] != new_l[2] and new_l[2] == new_l[3]:
    print("Yes")
else:
    print("No")