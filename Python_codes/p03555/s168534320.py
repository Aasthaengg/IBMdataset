C1 = input()
C2 = input()

c11 = C1[0]
c12 = C1[1]
c13 = C1[-1]

c21 = C2[0]
c22 = C2[1]
c23 = C2[-1]

if (c11 == c23) and (c13 == c21) and (c12 == c22):
    print("YES")

else:
    print("NO")

