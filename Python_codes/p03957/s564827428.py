s = input()
c_idx = s.find("C")
f_idx = s.rfind("F")
if c_idx != -1 and f_idx != -1 and f_idx-c_idx >0:
    print("Yes")
else:print("No")
