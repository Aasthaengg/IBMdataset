import sys
H=int(input())
a = 0
while   True:
    H=int(H/2)
    a=a+1
    #print(H) 
    if  H==0:
        print(2**a-1) 
        sys.exit()