s = input()

pos_a = s.find("A")
pos_z = s.rfind("Z")

print(pos_z -pos_a +1)