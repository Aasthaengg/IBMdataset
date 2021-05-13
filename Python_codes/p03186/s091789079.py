A,B,C = list(map(int,input().split()))
sum = 0
if B == C:
    sum += B*2
    B = 0
    C = 0
elif B > C:
    sum += C+B
    B -=C
    C = 0
else:
    sum += B*2
    C -=B
    B = 0
if A == C:
    sum += C
elif A > C:
    sum += C
else:
    sum += A+1
print(sum)
