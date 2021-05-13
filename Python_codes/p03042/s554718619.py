date=input()
if 1<=int(date[:2])<=12:
    if 1 <= int(date[2:]) <= 12:
        print("AMBIGUOUS")
        exit(0)
    else:
        print("MMYY")
        exit(0)
if int(date[2:])==0 or 13 <= int(date[2:]):
    print("NA")
    exit(0)
print("YYMM")