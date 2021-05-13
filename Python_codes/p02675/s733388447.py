n = int(input())

n1=n%10
if( n1==3 ):
    print("bon")
elif( n1==0 or n1==1 or n1==6 or n1==8):
    print("pon")
else:
    print("hon")