n=str(input())
jo=int(n[-1])
if jo==3:
    print("bon")
elif jo==0 or jo == 1 or jo==6 or jo==8:
    print("pon")
else:
    print("hon")