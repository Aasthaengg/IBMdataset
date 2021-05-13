A,B,C = input().split()

A = A[len(A)-1:len(A)]
Bf = B
Bl = B
Bf = Bf[0:1]
Bl = Bl[len(B)-1:len(B)]
C = C[0:1]

if A == Bf:
    if Bl == C:
        print("YES")
    else:
        print("NO")
else:
    print("NO")