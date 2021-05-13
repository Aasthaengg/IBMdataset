n = input()
l = n[-1]
m = int(l)
if m==3:
    print("bon")
elif m==0 or m==1 or m==6 or m==8:
    print("pon")
else: print("hon")