AA=list(input())

A=[int(n) for n in AA]
Q=sum(A)
B=Q-2*A[1]
C=Q-2*A[2]
D=Q-2*A[3]
E=Q-2*A[1]-2*A[2]
F=Q-2*A[1]-2*A[3]
G=Q-2*A[1]-2*A[2]-2*A[3]
H=Q-2*A[2]-2*A[3]
if Q==7:
    print(AA[0]+'+'+AA[1]+'+'+AA[2]+'+'+AA[3]+'='+'7')
elif B==7:
    print(AA[0]+'-'+AA[1]+'+'+AA[2]+'+'+AA[3]+'='+'7')
elif C==7:
    print(AA[0]+'+'+AA[1]+'-'+AA[2]+'+'+AA[3]+'='+'7')
elif D==7:
    print(AA[0]+'+'+AA[1]+'+'+AA[2]+'-'+AA[3]+'='+'7')
elif E==7:
    print(AA[0]+'-'+AA[1]+'-'+AA[2]+'+'+AA[3]+'='+'7')
elif F==7:
    print(AA[0]+'-'+AA[1]+'+'+AA[2]+'-'+AA[3]+'='+'7')
elif G==7:
    print(AA[0]+'-'+AA[1]+'-'+AA[2]+'-'+AA[3]+'='+'7')
elif H==7:
    print(AA[0]+'+'+AA[1]+'-'+AA[2]+'-'+AA[3]+'='+'7')