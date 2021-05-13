s=input()
n=len(s)
if n>9 or n<5:
    print("NO")
else:
    ans="NO"
    if n==5:
        if s=="KIHBR":
            ans="YES"
    elif n==6:
        if s=="AKIHBR" or s=="KIHABR" or s=="KIHBAR" or s=="KIHBRA":
            ans="YES"
    elif n==7:
        if s=="AKIHABR" or s=="AKIHBAR" or s=="AKIHBRA" or s=="KIHABAR" or s=="KIHABRA" or s=="KIHBARA":
            ans="YES"
    elif n==8:
        if s=="KIHABARA" or s=="AKIHBARA" or s=="AKIHABRA" or s=="AKIHABAR":
            ans="YES"
    else:
        if s=="AKIHABARA":
            ans="YES"
    print(ans)
