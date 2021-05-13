s = input()

c0 = s.count("0")
c1 = s.count("1")

print(min([c0*2,c1*2]))