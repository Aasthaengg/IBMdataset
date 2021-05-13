S = input()
a,b = int(S[:2]),int(S[2:])
if (1<=a and a<=12) or (1<=b and b<=12):
    if (1<=a and a<=12) and (1<=b and b<=12): 
        print("AMBIGUOUS")
    elif (1<=b and b<=12):
        print("YYMM")
    elif  (1<=a and a<=12): 
        print("MMYY")
  
else:
    print("NA")




