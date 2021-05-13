S = input()
month_list = ["01","02","03","04","04","05","06","07","08","09","10","11","12"]

if S[0:2] in month_list:
    if S[2:4] in month_list:
        print("AMBIGUOUS")
    else:
        print("MMYY")

else:
    if S[2:4] in month_list:
        print("YYMM")
    else:
        print("NA")