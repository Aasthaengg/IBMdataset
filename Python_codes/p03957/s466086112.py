s = input()

if "C" in s and "F" in s and s.find("C") < s.find("F", s.find("C")):
    print("Yes")
else:
    print("No")
