S=input()
x=int(S[:2])
y=int(S[2:])

if 0<x<13 and 0<y<13:print("AMBIGUOUS")
elif 0<x<13:print("MMYY")
elif 0<y<13:print("YYMM")
else:print("NA")