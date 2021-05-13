#11
import sys
A,B,C = map(int,input().split())

a1,b1,c1,cou= 0,0,0,0



while A%2 == 0 and B%2 == 0 and C%2 == 0:
    if A == B == C:
        print("-1")
        sys.exit()
    a1 = int(A/2) 
    b1 = int(B/2) 
    c1 = int(C/2) 
    A = b1+c1
    B = a1+c1
    C = a1+b1
    cou += 1
    
print(cou)