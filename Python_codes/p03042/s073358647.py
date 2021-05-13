s=input()

first = int(s[:2])
second = int(s[2:])

if (first>0) and (first<13) and (second>0) and (second<13):
    print("AMBIGUOUS")
elif (first>0) and (first<13) and ((second==0) or (second>=13)):
    print("MMYY")
elif (second>0) and (second<13) and ((first==0) or (first>=13)):
    print("YYMM")
else:
    print("NA")