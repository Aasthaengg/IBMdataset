N=int(input())
M=N%10
#print(M)
if M==2 or M==4 or M==5 or M==7 or M==9:
    print("hon")
if M==0 or M==1 or M==6 or M==8:
    print("pon")
if M==3:
    print("bon")