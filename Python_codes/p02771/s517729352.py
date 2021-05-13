x=list((int(x) for x in input().split()))
if(len(set(x))==2):
    print("Yes")
else:
    print("No")