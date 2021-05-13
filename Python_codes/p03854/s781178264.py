s = input()
a = s.replace("eraser","")
b = a.replace("erase","")
c = b.replace("dreamer","")
d = c.replace("dream","")
if d == "":
    print("YES")
else:
    print("NO")