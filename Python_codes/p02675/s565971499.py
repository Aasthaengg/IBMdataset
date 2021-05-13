a = int(input())
b = str(a)
B = int(b[-1])
if B==3:
    print("bon")
elif B==0 or B==1 or B==6 or B==8:
    print("pon")
else:
    print("hon")