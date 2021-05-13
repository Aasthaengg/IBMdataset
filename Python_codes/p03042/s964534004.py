S=input()
s=list(S)
left=int(s[0])*10+int(s[1])
right=int(s[2])*10+int(s[3])
if 1<=left<=12:
    if 1<=right<=12:
        print("AMBIGUOUS")
    else:
        print("MMYY")
else:
    if 1<=right<=12:
        print("YYMM")
    else:
        print("NA")