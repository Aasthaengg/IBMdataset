import re
a=input()
b=re.fullmatch(r"(\d{4})/(\d{2})/(\d{2})",a)
if int(b.group(1))<2019:
    print("Heisei")

elif int(b.group(1))==2019:
    if int(b.group(2))<=4:
        print("Heisei")

    else:
        print("TBD")

else:
    print("TBD")