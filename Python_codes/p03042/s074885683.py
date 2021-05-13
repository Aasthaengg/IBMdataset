s=input()
if (0<=int(s[:2])<=99 and 1<=int(s[2:])<=12) and not(0<=int(s[2:])<=99 and 1<=int(s[:2])<=12):
    print("YYMM")
elif (0<=int(s[2:])<=99 and 1<=int(s[:2])<=12) and not((0<=int(s[:2])<=99 and 1<=int(s[2:])<=12)):
    print("MMYY")
elif (0<=int(s[:2])<=99 and 1<=int(s[2:])<=12) and (0<=int(s[2:])<=99 and 1<=int(s[:2])<=12):
    print("AMBIGUOUS")
else:
    print("NA")