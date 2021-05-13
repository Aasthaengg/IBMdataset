s=input()
if "C"not in s:print("No")
elif s.find("C",0)<s.find("F",s.find("C",0)+1):print("Yes")
else:print("No")