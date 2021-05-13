N = int(input())
A,B,C = 0,0,0
for TA in range(1,3501):
    for TB in range(1,3501):
        Numer = TA*TB*N
        Denom = 4*TA*TB-(TA+TB)*N
        if Denom>0 and Numer>0 and Numer%Denom==0:
            A = TA
            B = TB
            C = Numer//Denom
print('{} {} {}'.format(A,B,C))