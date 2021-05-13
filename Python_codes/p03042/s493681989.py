s = list(input())

a = 10*int(s[0])+int(s[1])
b = 10*int(s[2])+int(s[3])

if 0<a<13 and 0<b<13:
    print("AMBIGUOUS")
elif 0<a<13:
    print("MMYY")
elif 0<b<13:
    print("YYMM")
else:
    print("NA")