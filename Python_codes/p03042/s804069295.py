s=int(input())
s1=s//100
s2=s-s1*100
if 0<s1<=12 and 0<s2<=12:
    print("AMBIGUOUS")
elif (s1>12 or s1==0) and 0<s2<=12:
    print("YYMM")
elif 0<s1<=12 and (s2>12 or s2==0):
    print("MMYY")
else:
    print("NA")