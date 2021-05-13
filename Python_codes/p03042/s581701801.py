n=input()

n1,n2=int(n[:2]),int(n[2:])
#if (n1>12 and n2>12) or (n1==0 and n2==0):
#   print("NA")
if (n1!=0 and n1<=12) and (n2!=0 and n2<=12):
    print("AMBIGUOUS")
elif n1!=0 and n1<=12:
    print("MMYY")
elif n2!=0 and n2<=12:
    print("YYMM")
else:
    print("NA")



