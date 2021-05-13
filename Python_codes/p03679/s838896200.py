X,A,B = [int(i) for i in input().split()]

if (B <= A) :
    print("delicious")
elif (B-A <= X) :
    print("safe")
else :
    print("dangerous")