S = input()
 
 
D = S.count("R")
 
if D == 1:
    print(1)
 
elif D == 3:
    print(3)
 
elif D == 2:
    for i in range(3):
        if S[i] =="R":
            if S[i+1] =="R":
                print(2)
                break
 
            else:
                print(1)
                break
 
elif D == 0:
    print(0)    
