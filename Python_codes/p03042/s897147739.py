s = input()
if (int(s[:2]) == 0 or int(s[:2]) > 12)&(0 < int(s[2:]) <= 12):
    print("YYMM")
    
elif (0 < int(s[:2]) <= 12)&(int(s[2:]) == 0 or int(s[2:]) > 12):
    print("MMYY")

elif (0 < int(s[:2]) <= 12)&(0 < int(s[2:]) <= 12):
    print("AMBIGUOUS")

else:
    print("NA")