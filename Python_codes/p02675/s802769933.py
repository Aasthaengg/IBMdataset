N=input()
N=list(map(int,N))

if N[-1]==2 or N[-1]==4 or N[-1]==5 or N[-1]==7 or N[-1]==9:
    print("hon")
elif N[-1]==0 or N[-1]==1 or N[-1]==6 or N[-1]==8:
    print("pon")
elif N[-1]==3:
    print("bon")