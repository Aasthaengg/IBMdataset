s=input()

if int(s[:4]) < 2019:
    print("Heisei")
else:
    if s[5:7] in ["01","02","03","04"]:
        print("Heisei")
    else:
        print("TBD")
        
