line = input().split()
l = [int(s) for s in line]



if -100 <= l[0] <= l[2] <= l[1]<=100:
    
    print("Yes")
    
else:
    print("No")