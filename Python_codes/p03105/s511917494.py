n=input().split()
A=int(n[0])
B=int(n[1])
C=int(n[2])

if B>=A*C:
    print(C)
elif B<A*C:
    print(B//A)