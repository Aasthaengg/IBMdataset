S=input()
Y=int(S[:2])
M=int(S[2:])
if Y==0 or Y>12:
    #Y!=MANTH
    if M==0 or M>12:
        print("NA")
    else:
        print("YYMM")
else:
    if M==0 or M>12:
        print("MMYY")
    else:
        print("AMBIGUOUS")
