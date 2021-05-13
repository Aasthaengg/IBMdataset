S=input()
x=int(S[:2])
y=int(S[2:])
if x==0:
    if 0<y<=12:
        print("YYMM")
    else:
        print("NA")
elif 0<x<=12:
    if 0<y<=12:
        print("AMBIGUOUS")
    else:
        print("MMYY")
elif x>=13:
    if 0<y<=12:
        print("YYMM")
    else:
        print("NA")