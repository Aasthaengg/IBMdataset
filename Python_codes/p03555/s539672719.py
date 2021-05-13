C1 = input()
R1 = C1[::-1]
C2 = input()
R2 = C2[::-1]
print(['NO','YES'][R2==C1 and R1==C2])