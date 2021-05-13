s = input()

pc = s.find("C")
if -1 < pc and -1 < s.find("F", pc): 
    print("Yes")
else:
    print("No")
