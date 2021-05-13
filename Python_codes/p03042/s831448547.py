# 126 B

s = input()

fir = int(s[:2])
sec = int(s[2:])

if fir > 0 or sec > 0:
    if 1 <= fir <= 12 and 1 <= sec <= 12 :
        print("AMBIGUOUS")
    elif 1 <= fir <= 12: 
        print("MMYY")
    elif 1 <= sec <= 12:
        print("YYMM") 
    else:
        print("NA")
else:
    print("NA")
