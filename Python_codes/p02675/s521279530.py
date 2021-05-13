#Write your code in below
Num = str(input().rstrip())
if int(Num[-1]) ==3:
    print("bon")
elif int(Num[-1]) in [0,1,6,8]:
    print("pon")
else:
    print("hon")
