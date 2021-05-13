a=int(input())
l=a/100
r=a%100
if 1<=l and l<=12:
    if 1<=r and  r<=12:
        print("AMBIGUOUS")
    else:
        print("MMYY")
else:
    if 1<=r and r<=12:
        print("YYMM")
    else:
        print("NA")