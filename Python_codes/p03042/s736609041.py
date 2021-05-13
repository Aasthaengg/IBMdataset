s = input()

aa = int(s[0])*10 + int(s[1])
bb = int(s[2])*10 + int(s[3])

if 1 <= aa <= 12 and 1 <= bb <= 12 :
    print("AMBIGUOUS")
elif 1 <= aa <= 12 and bb == 0 :
    print("MMYY")
elif 1 <= aa <= 12 and 13 <= bb :
    print("MMYY")
elif aa == 0 and 1<= bb <= 12 :
    print("YYMM")
elif 13<=aa and 1<=bb<=12 :
    print("YYMM")
else :
    print("NA")
