s = input()
n0 = s.count("0")
n1 = s.count("1")
print(len(s) - abs(n0-n1))