S = int(input())  
    
if S == 10**18:
    X2 = 10**9
    Y3 = 10**9
    Y2 = 0
    X3 = 0
elif S > 10**9:
    r = 10**9 - (S % 10**9)
    Y2 = r
    X3 = 1
    S += r
    X2 = S //10**9
    Y3 = 10**9
else:
    Y2 = 0
    X3 = 0
    X2 = S
    Y3 = 1

        
print(0, 0, X2, Y2, X3, Y3)