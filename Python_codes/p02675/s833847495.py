v=int(input())

v=v%10
if v==3:
    print("bon")
elif v==0 or v==1 or v==6 or v==8:
    print("pon")
else:
    print("hon")
