s=input()
if int(s[:2])<=12 and int(s[:2])>0:
    if int(s[2:4])<=12 and int(s[2:4])>0:
        print("AMBIGUOUS")
    else:
        print("MMYY")
elif int(s[2:4])<=12 and int(s[2:4])>0:
    print("YYMM")
else:
    print("NA")