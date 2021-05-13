s=(input())
s1=int(s[:2])
s2=int(s[2:])
 
if 1<= s1 <=12 and 1<= s2 <= 12:
    print("AMBIGUOUS")
 
elif 0<= s1 <=99 and 1<= s2 <= 12:
    print("YYMM")
 
elif 1<= s1 <=12 and 0<= s2 <= 99:
    print("MMYY")
 
else:
    print("NA")