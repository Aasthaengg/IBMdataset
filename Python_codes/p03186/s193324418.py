A , B , C = map(int, input().split())  

EAT = B
if  A + B > C:
    EAT += C
elif A + B == C:
    EAT += C
else :
    EAT += A + B + 1

print(EAT)




