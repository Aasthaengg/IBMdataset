s=list(input())
s1="".join(s[:2])
s2="".join(s[2:])
if 0<int(s1)<=12 and 0<int(s2)<=12:
    print("AMBIGUOUS")
elif 0<int(s1)<=12 and (int(s2)>12 or int(s2)==0):
    print("MMYY")
elif 0<int(s2)<=12 and (int(s1)>12 or int(s1)==0):
    print("YYMM")
else:
    print("NA")