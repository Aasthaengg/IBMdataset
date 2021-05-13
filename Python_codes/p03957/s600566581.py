s=input()
if "C" in s and "F" in s and s.find("C")<len(s)-1-s[::-1].find("F"):
    print("Yes")

else: print("No")